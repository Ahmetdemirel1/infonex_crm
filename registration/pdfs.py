import os
import pytz
from functools import partial
from itertools import zip_longest
from math import ceil

from django.db.models import Count, Sum
from django.utils import timezone

from .constants import *
from delegate.constants import UNPAID_STATUS_VALUES
from infonex_crm.settings import BASE_DIR

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image
from reportlab.platypus.flowables import HRFlowable

LOGO_PATH = os.path.join(BASE_DIR,
                         'delegate/static/delegate/INFONEX-logo-tag.jpg')
CHECKBOX_PATH = os.path.join(BASE_DIR,
                             'crm/static/crm/images/checkbox.jpg')
PAGE_HEIGHT = letter[1]
PAGE_WIDTH = letter[0]


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_footer(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_footer(self, page_count):
        width, height = self._pagesize
        print_date = timezone.now().strftime('%-d %B, %Y')
        # Change the position of this to wherever you want the page number to be
        self.setFont('Helvetica-Bold', 10)
        self.drawString(36, 0.5 * inch,
                        "Page %d of %d" % (self._pageNumber, page_count))
        self.drawRightString(width - 36, 0.5 * inch, print_date)
        copyright_notice = '©' + timezone.now().strftime('%Y') + ' Infonex Inc.'
        self.drawCentredString(width / 2, 0.5 * inch, copyright_notice)


class ConferenceReportPdf:
    """
    Class to manage generation and delivery of pdfs
    """

    def __init__(self, buffer, event, sort='company'):
        self._buffer = buffer
        self._pagesize = letter
        self._width, self._height = self._pagesize
        self._event = event
        self._sort = sort

    def generate_delegate_list(self):
        report_name = 'Delegate List - CONFIDENTIAL'
        buffer = self._buffer
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.6 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        header_style = styles['h4']
        header_style.alignment = TA_LEFT
        cell_style = styles['BodyText']
        cell_style.alignment = TA_LEFT
        table_data.append([
            Paragraph('Delegate Name', header_style),
            Paragraph('Title', header_style),
            Paragraph('Company', header_style)
        ])
        if self._sort == 'name':
            sorts = ['registrant__last_name',
                     'registrant__first_name',
                     'registrant__company__name']
        elif self._sort == 'title':
            sorts = ['registrant__title',
                     'registrant__company__name',
                     'registrant__last_name',
                     'registrant__first_name']
        else:
            sorts = ['registrant__company__name',
                     'registrant__title',
                     'registrant__last_name',
                     'registrant__first_name']
        reg_list = self._event.regdetails_set.all().order_by(*sorts)
        for i, reg_detail in enumerate(reg_list):
            name = Paragraph(
                reg_detail.registrant.first_name + ' ' + \
                    reg_detail.registrant.last_name,
                cell_style
            )
            title = Paragraph(
                reg_detail.registrant.title,
                cell_style
            )
            company = Paragraph(
                reg_detail.registrant.company.name,
                cell_style
            )
            table_data.append([name, title, company])
        table = Table(table_data,
                      colWidths=[doc.width/3.0]*3,
                      repeatRows=1)
        table.setStyle(TableStyle([
            ('LINEABOVE', (0,0), (-1, 0), 2, colors.black),
            ('LINEBELOW', (0,0), (-1, 0), 1, colors.black),
            ('VALIGN', (0,0), (-1, -1), 'TOP'),
        ]))
        elements.append(table)
        doc.build(elements,
                  onFirstPage=partial(self._header, event=self._event,
                                      report_title = report_name),
                  onLaterPages=partial(self._header, event=self._event,
                                       report_title = report_name),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def generate_no_name_list(self):
        report_name = 'Delegate List - CONFIDENTIAL'
        buffer = self._buffer
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.6 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        header_style = styles['h4']
        header_style.alignment = TA_LEFT
        cell_style = styles['BodyText']
        cell_style.alignment = TA_LEFT
        table_data.append([
            Paragraph('Title', header_style),
            Paragraph('Company', header_style)
        ])
        if self._sort == 'title':
            sorts = ['registrant__title',
                     'registrant__company__name']
        else:
            sorts = ['registrant__company__name',
                     'registrant__title']
        reg_list = self._event.regdetails_set.all().order_by(*sorts)
        for i, reg_detail in enumerate(reg_list):
            title = Paragraph(
                reg_detail.registrant.title,
                cell_style
            )
            company = Paragraph(
                reg_detail.registrant.company.name,
                cell_style
            )
            table_data.append([title, company])
        table = Table(table_data,
                      colWidths=[doc.width/2.0]*2,
                      repeatRows=1)
        table.setStyle(TableStyle([
            ('LINEABOVE', (0,0), (-1, 0), 2, colors.black),
            ('LINEBELOW', (0,0), (-1, 0), 1, colors.black),
            ('VALIGN', (0,0), (-1, -1), 'TOP'),
        ]))
        elements.append(table)
        doc.build(elements,
                  onFirstPage=partial(self._header, event=self._event,
                                      report_title = report_name),
                  onLaterPages=partial(self._header, event=self._event,
                                       report_title = report_name),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def generate_registration_list(self):
        report_name = 'Registration List - CONFIDENTIAL'
        buffer = self._buffer
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.6 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        cell_style_left = ParagraphStyle(
            name='cellLeft',
            fontName='Helvetica',
            fontSize=9,
            leading=11,
            alignment=TA_LEFT,
        )
        cell_style_right = ParagraphStyle(
            name='cellRight',
            fontName='Helvetica',
            fontSize=9,
            leading=11,
            alignment=TA_RIGHT,
        )
        if self._sort == 'name':
            sorts = ['registrant__last_name',
                     'registrant__first_name',
                     'registrant__company__name']
        elif self._sort == 'title':
            sorts = ['registrant__title',
                     'registrant__company__name',
                     'registrant__last_name',
                     'registrant__first_name']
        else:
            sorts = ['registrant__company__name',
                     'registrant__title',
                     'registrant__last_name',
                     'registrant__first_name']
        # reg_list = self._event.regdetails_set.all().order_by(*sorts)
        reg_list = self._event.regdetails_set.filter(
            invoice__isnull=False
        ).order_by(*sorts)
        for i, reg_detail in enumerate(reg_list):
            invoice_total = reg_detail.invoice.pre_tax_price + \
                reg_detail.invoice.pre_tax_price * \
                    reg_detail.invoice.gst_rate + \
                reg_detail.invoice.pre_tax_price * \
                    reg_detail.invoice.hst_rate + \
                reg_detail.invoice.pre_tax_price * \
                    (1 + reg_detail.invoice.gst_rate) * \
                    reg_detail.invoice.qst_rate
            cell1 = Paragraph(
                reg_detail.get_registration_status_display() + '<br/>' + \
                    reg_detail.register_date.strftime('%-d %B, %Y') + \
                    '<br/>Inv#: ' + str(reg_detail.invoice.pk),
                cell_style_left
            )
            cell2 = [
                Paragraph(
                    str('${:,.2f}'.format(reg_detail.invoice.pre_tax_price)) + \
                        '<br/>+ Tax<br/>',
                    cell_style_right
                ),
                HRFlowable(width='100%', thickness=1, color=colors.black),
                Paragraph(
                    '<b>' + str('${:,.2f}'.format(invoice_total)) + '</b>',
                    cell_style_right
                )
            ]
            cell3 = Paragraph(
                reg_detail.registrant.first_name + ' ' + \
                    reg_detail.registrant.last_name + '<br/>' + \
                    reg_detail.registrant.title + '<br/>' +
                    reg_detail.registrant.company.name,
                cell_style_left
            )
            location = ''
            if reg_detail.registrant.company.city:
                location += reg_detail.registrant.company.city
            location += '<br/>'
            if reg_detail.registrant.company.state_prov:
                location += reg_detail.registrant.company.state_prov
            cell4 = Paragraph(location, cell_style_left)
            cell5 = Paragraph(
                'Sales:<br/>Paid:', cell_style_right
            )
            if reg_detail.invoice.payment_date:
                pymt_date = reg_detail.invoice.payment_date.strftime(
                    '%-d %B, %Y'
                )
            else:
                pymt_date = ''
            cell6 = Paragraph(
                reg_detail.invoice.sales_credit.username + '<br/>' + pymt_date,
                cell_style_left
            )
            table_data.append([cell1, cell2, cell3, cell4, cell5, cell6])
        if len(table_data) > 0:
            table = Table(table_data,
                          colWidths=[cm * 3.5, cm * 3, cm * 4.5,
                                     cm * 3, cm * 2, cm * 3])
            table.setStyle(TableStyle([
                ('LINEABOVE', (0,0), (-1, 0), 2, colors.black),
                ('LINEBELOW', (0,0), (-1, -1), 1, colors.black),
                ('VALIGN', (0,0), (-1, -1), 'TOP'),
            ]))
            elements.append(table)
        else:
            notice_style = styles['h2']
            notice_style.alignment = TA_CENTER
            elements.append(Paragraph('No delegates', notice_style))
        doc.build(elements,
                  onFirstPage=partial(self._header, event=self._event,
                                      report_title = report_name),
                  onLaterPages=partial(self._header, event=self._event,
                                       report_title = report_name),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def generate_phone_list(self):
        report_name = 'Phone/Email List'
        buffer = self._buffer
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.6 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        delegate_style = ParagraphStyle(
            name='delegateStyle',
            fontName='Helvetica',
            fontSize=12,
            leading=14,
            alignment=TA_LEFT,
        )
        label_style = ParagraphStyle(
            name='labelStyle',
            fontName='Helvetica-Bold',
            fontSize=12,
            leading=14,
            alignment=TA_RIGHT,
        )
        if self._sort == 'name':
            sorts = ['registrant__last_name',
                     'registrant__first_name',
                     'registrant__company__name']
        elif self._sort == 'title':
            sorts = ['registrant__title',
                     'registrant__company__name',
                     'registrant__last_name',
                     'registrant__first_name']
        else:
            sorts = ['registrant__company__name',
                     'registrant__title',
                     'registrant__last_name',
                     'registrant__first_name']
        reg_list = self._event.regdetails_set.filter(
            invoice__isnull=False
        ).order_by(*sorts)
        elements = []
        elements.append(
            HRFlowable(width='100%', thickness=2, color=colors.black)
        )
        for i, reg_detail in enumerate(reg_list):
            table1_data = [[
                Paragraph(reg_detail.registrant.first_name + ' ' + \
                            reg_detail.registrant.last_name,
                          delegate_style),
                Paragraph(reg_detail.registrant.title, delegate_style),
                Paragraph(reg_detail.registrant.company.name, delegate_style)
            ]]

            table2_data = [[
                Paragraph('Phone 1:<br/>Phone 2:', label_style),
                Paragraph(reg_detail.registrant.phone1 + '<br/>' + \
                              reg_detail.registrant.phone2,
                          delegate_style),
                Paragraph('Email 1:<br/>Email 2:', label_style),
                Paragraph(reg_detail.registrant.email1 + '<br/>' + \
                              reg_detail.registrant.email2,
                          delegate_style)
            ]]

            table1 = Table(table1_data,
                           colWidths=[6.22 * cm]*3)
            table2 = Table(table2_data,
                           colWidths=[cm * 2.3, cm * 5.46, cm * 2.3, cm * 8.6])
            if i > 0:
                table1.setStyle(TableStyle([
                    ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                ]))
            else:
                table1.setStyle(TableStyle([
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
                ]))
            table2.setStyle(TableStyle([
                ('LINEBELOW', (0,-1), (-1,-1), 1, colors.black),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ]))
            elements.append(table1)
            elements.append(table2)
        # else:
        #     notice_style = styles['h2']
        #     notice_style.alignment = TA_CENTER
        #     elements.append(Paragraph('No delegates', notice_style))
        doc.build(elements,
                  onFirstPage=partial(self._header, event=self._event,
                                      report_title = report_name),
                  onLaterPages=partial(self._header, event=self._event,
                                       report_title = report_name),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def generate_unpaid_list(self):
        buffer = self._buffer
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.8 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        header_style = ParagraphStyle(
            name='cellHeader',
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
        )
        cell_style = ParagraphStyle(
            name='cellStyle',
            fontName='Helvetica',
            fontSize=12,
            leading=14,
            alignment=TA_LEFT,
        )
        table_data.append([
            Paragraph('Delegate Name', header_style),
            Paragraph('Company', header_style),
            Paragraph('Payment Received', header_style),
            Paragraph('Signature', header_style),
        ])
        if self._sort == 'name':
            sorts = ['registrant__last_name',
                     'registrant__first_name',
                     'registrant__company__name']
        else:
            sorts = ['registrant__company__name',
                     'registrant__last_name',
                     'registrant__first_name']
        reg_list = self._event.regdetails_set.filter(
            invoice__isnull=False,
            registration_status__in=UNPAID_STATUS_VALUES,
        ).order_by(*sorts)
        max_height = inch * 0.5
        for i, reg_detail in enumerate(reg_list):
            name = Paragraph(
                reg_detail.registrant.last_name + ', ' + \
                    reg_detail.registrant.first_name,
                cell_style
            )
            company = Paragraph(
                reg_detail.registrant.company.name,
                cell_style
            )
            table_data.append([name, company, '', ''])
            cell_height = name.wrap(doc.width/4.0 - 12, inch * 9.0)[1]
            if cell_height > max_height:
                max_height = cell_height
            cell_height = company.wrap(doc.width/4.0 - 12, inch * 9.0)[1]
            if cell_height > max_height:
                max_height = cell_height
        table = Table(table_data,
                      colWidths=[doc.width/4.0]*4,
                      rowHeights=[inch * 0.3] + [max_height + 6] * reg_list.count(),
                      repeatRows=1)
        table.setStyle(TableStyle([
            ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
            ('BOX', (0,0), (-1,-1), 1, colors.black),
            ('VALIGN', (0,0), (-1, -1), 'TOP'),
        ]))
        elements.append(table)
        doc.build(elements,
                  onFirstPage=partial(self._unpaid_list_header,
                                      event=self._event),
                  onLaterPages=partial(self._unpaid_list_header,
                                       event=self._event),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def generate_onsite_list(self):
        report_name = 'Onsite Delegate Checklist'
        buffer = self._buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.0 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        header_style = ParagraphStyle(
            name='cellHeader',
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
        )
        cell_style = ParagraphStyle(
            name='cellStyle',
            fontName='Helvetica',
            fontSize=9,
            leading=13,
            alignment=TA_LEFT,
        )
        table_data.append([
            Paragraph('Name', header_style),
            Paragraph('Company', header_style),
            Paragraph('Day 1', header_style),
            Paragraph('Day 2', header_style),
        ])
        sorts = ['registrant__last_name',
                 'registrant__first_name',
                 'registrant__company__name']
        reg_list = self._event.regdetails_set.all().order_by(*sorts)
        max_height = inch * 0.2
        for i, reg_detail in enumerate(reg_list):
            name = Paragraph(
                '<b>' + reg_detail.registrant.first_name + ' ' + \
                    reg_detail.registrant.last_name + '</b><br/>' + \
                    reg_detail.get_registration_status_display(),
                cell_style
            )
            company = Paragraph(
                reg_detail.registrant.company.name + '<br/>' + \
                    reg_detail.registrant.phone1,
                cell_style
            )
            checkbox = Image(CHECKBOX_PATH)
            checkbox.drawHeight = cm * 0.5
            checkbox.drawWidth = cm * 0.5
            table_data.append([name, company, checkbox, checkbox])
            cell_height = name.wrap(doc.width/4.0 - 12, inch * 9.0)[1]
            if cell_height > max_height:
                max_height = cell_height
            cell_height = company.wrap(doc.width/4.0 - 12, inch * 9.0)[1]
            if cell_height > max_height:
                max_height = cell_height
        table = Table(table_data,
                      colWidths=[doc.width / 3.0] * 2 + [doc.width / 6.0] * 2,
                      rowHeights=[inch * 0.3] + [max_height + 6] * reg_list.count(),
                      repeatRows=1)
        table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1, 0), 'TOP'),
            ('VALIGN', (0,1), (1, -1), 'TOP'),
            ('VALIGN', (2, 1), (-1, -1), 'MIDDLE'),
            ('LINEABOVE', (0,0), (-1, 0), 2, colors.black),
            ('LINEBELOW', (0,0), (-1, -1), 1, colors.black),

        ]))
        elements.append(table)
        doc.build(elements,
                  onFirstPage=partial(self._small_header,
                                      event=self._event,
                                      report_title=report_name),
                  onLaterPages=partial(self._small_header,
                                       event=self._event,
                                       report_title=report_name),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def generate_ce_sign_in_sheet(self):
        report_name = 'Sign-in Sheet for CE Credits'
        buffer = self._buffer
        event_has_options = self._event.eventoptions_set.exists()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.0 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        header_style = ParagraphStyle(
            name='headerStyle',
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=12,
            alignment=TA_CENTER,
        )
        person_style = ParagraphStyle(
            name='personStyle',
            fontName='Helvetica',
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
        )
        label_style = ParagraphStyle(
            name='labelStyle',
            fontName='Helvetica',
            fontSize=10,
            leading=12,
            alignment=TA_RIGHT,
        )
        table_data.append([
            Paragraph('', header_style),
            Paragraph('', header_style),
            Paragraph('Time', header_style),
            Paragraph('Initials', header_style),
        ])
        sorts = ['registrant__last_name',
                 'registrant__first_name',
                 'registrant__company__name']
        reg_list = self._event.regdetails_set.all().order_by(*sorts)
        max_height = inch * 0.2
        for i, reg_detail in enumerate(reg_list):
            person_name = '<b>' + reg_detail.registrant.first_name + ' ' + \
                reg_detail.registrant.last_name + '</b><br/>'
            if reg_detail.registrant.title:
                person_name += reg_detail.registrant.title + '<br/>'
            if reg_detail.registrant.company.name:
                person_name += reg_detail.registrant.company.name
            person = Paragraph(
                person_name,
                person_style
            )

            self._label = '<br/>'
            self._line_groups = []  # List to show where to put extra <br/>s
            if event_has_options:
                self._make_sign_in_label_list(reg_detail)
            else:
                self._label += 'Day One Arrival:<br/><br/>' + \
                    'Departure:<br/><br/>' + \
                    'Day Two Arrival:<br/><br/>' + \
                    'Departure:<br/><br/><br/>'
                self._line_groups.append(4)
            self._label = self._label[:-5]  # remove last <br/> tag
            labels = Paragraph(self._label, label_style)

            info_lines = '<br/> '
            for line_group in self._line_groups:
                for i in range(line_group):
                    info_lines += '_' * 20 + ' <br/><br/> '
                info_lines += '<br/>'
            line_para = Paragraph(info_lines, header_style)

            table_data.append([person, labels, line_para, line_para])
            cell_height = person.wrap(doc.width/4.0 - 12, inch * 9.0)[1]
            if cell_height > max_height:
                max_height = cell_height
            cell_height = labels.wrap(doc.width/4.0 - 12, inch * 9.0)[1]
            if cell_height > max_height:
                max_height = cell_height
        table = Table(table_data,
                      colWidths=[doc.width / 4.0] * 4,
                      rowHeights=[inch * 0.3] + [max_height + 6] * reg_list.count(),
                      repeatRows=1)
        table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1, 0), 'TOP'),
            ('VALIGN', (0,1), (-1, -1), 'TOP'),
            ('LINEABOVE', (0,0), (-1, 0), 2, colors.black),
            ('LINEBELOW', (0,0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        doc.build(elements,
                  onFirstPage=partial(self._small_header,
                                      event=self._event,
                                      report_title=report_name),
                  onLaterPages=partial(self._small_header,
                                       event=self._event,
                                       report_title=report_name),
                  canvasmaker=NumberedCanvas)

        pdf = buffer.getvalue()
        return pdf

    def badges(self, badge_type='bigCompany'):
        buffer = self._buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=cm,
                                leftMargin=0,
                                topMargin=0,
                                bottomMargin=0,
                                pagesize=self._pagesize)
        elements = []
        table_data = []
        badge_style = ParagraphStyle(  # last name on regular badges, full name on big company badges
            name='mediumStyle',
            fontName='Helvetica',
            fontSize=18,
            leading=28,
            alignment=TA_CENTER,
        )
        sorts = ['registrant__last_name',
                 'registrant__first_name',
                 'registrant__company__name']
        reg_list = self._event.regdetails_set.all().order_by(*sorts)
        num_rows = ceil(reg_list.count() / 2)
        badge_row = []
        print('count: ', reg_list.count())
        for reg in reg_list:
            if badge_type == 'bigCompany':
                badge_text = '<font size=18>' + reg.registrant.first_name + \
                    ' ' + reg.registrant.last_name + '</font><br/>' + \
                    '<font size=24><b>' + reg.registrant.company.name + \
                    '</b></font>'
            else:
                badge_text = '<font size = 24>' + reg.registrant.first_name + \
                    '</font><br/>' + reg.registrant.last_name + '<br/>'
                if reg.registrant.company.name:
                    badge_text += '<font size=14>' + \
                        reg.registrant.company.name + '</font>'
            badge = Paragraph(badge_text, badge_style)
            badge_row.append(badge)
            if len(badge_row) == 2:
                table_data.append(badge_row)
                badge_row = []
        if len(table_data) > 0:
            table = Table(table_data,
                          colWidths=[doc.width/2.0] * 2,
                          rowHeights=[cm * 7]* num_rows)
            table.setStyle(TableStyle([
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                ('TOPPADDING', (0,0), (-1, -1), inch),
                ('LEFTPADDING', (0,0), (-1, -1), cm),
                ('RIGHTPADDING', (0,0), (-1, -1), cm),
                ('BOTTOMPADDING', (0,0), (-1, -1), cm),
            ]))
            elements.append(table)
        doc.build(elements)
        pdf = buffer.getvalue()
        return pdf

    def delegate_count(self):
        report_name = 'Attendee Count'
        event_has_options = self._event.eventoptions_set.exists()
        buffer = self._buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=inch / 2,
                                leftMargin=inch / 2,
                                topMargin=1.6 * inch,
                                bottomMargin=inch * 0.75,
                                pagesize=self._pagesize)
        title_style = ParagraphStyle(
            name='titleStyle',
            fontName='Helvetica-Bold',
            fontSize=16,
            leading=18,
            alignment=TA_CENTER
        )
        label_cell_style = ParagraphStyle(
            name='labelCellStyle',
            fontName='Helvetica',
            fontSize=12,
            leading=16,
            alignment=TA_RIGHT
        )
        count_cell_style = ParagraphStyle(
            name='counteCellStyle',
            fontName='Helvetica',
            fontSize=12,
            leading=16,
            alignment=TA_LEFT
        )
        elements = []
        table_data = []

        counts_by_option = []
        if event_has_options:
            for option in EventOptions.objects.filter(event=self._event):
                counts_by_option.append(
                    [option.name,
                     RegDetails.objects.filter(eventoptions=option).annotate(
                         total=Count('registration_status')
                     ).order_by('total')]
                )
        else:
            counts_by_option.append([
                'Conference',
                RegDetails.objects.filter(
                    conference=self._event
                ).values('registration_status').annotate(
                    total=Count('registration_status')
                ).order_by('total')
            ])
            # del_counts = RegDetails.objects.filter(
            #     conference=self._event
            # ).values('registration_status').annotate(
            #     total=Count('registration_status')
            # ).order_by('total')
        for count in counts_by_option:
            labels=''
            counts=''
            for total in count[1]:
                labels += total.get_registration_status_display() + ':<br/>'
                counts += str(total.total) + '<br/>'
            cell1 = [
                Paragraph(labels, label_cell_style),
                HRFlowable(width='100%', thickness=1, color=colors.black),
                Paragraph('<b>Grand Total:</b>', label_cell_style)
            ]
            cell2 = [
                Paragraph(counts, count_cell_style),
                HRFlowable(width='100%', thickness=1, color=colors.black),
                Paragraph('<b>' + total.aggregate(Sum('total') + '</b>'),
                          count_cell_style)
            ]
            elements.append(Paragraph(count[0], title_style))
            table_data.append([cell1, cell2])


    @staticmethod
    def _header(canvas, doc, event, report_title):
        canvas.saveState()
        styles = getSampleStyleSheet()
        canvas.drawImage(LOGO_PATH, 0.45 * inch, PAGE_HEIGHT - inch * 0.75,
                         height=0.5*inch, width=1.875*inch)
        canvas.setFont('Helvetica-Bold', 18)
        y_coord = PAGE_HEIGHT - inch * 0.45
        canvas.drawString(2.75 * inch, y_coord, report_title)
        canvas.setFont('Helvetica', 16)
        event_title = str(event.number) + ' - ' + event.title
        y_coord -= 18
        canvas.drawString(2.75 * inch, y_coord, event_title)
        event_date = event.date_begins.strftime('%-d %B, %Y')
        y_coord -= 14
        canvas.setFont('Helvetica', 12)
        canvas.drawString(2.75 * inch, y_coord, event_date)
        event_venue = ''
        if event.hotel:
            event_venue += event.hotel.name + ': '
        event_venue += event.city + ', ' + event.state_prov
        y_coord -= 14
        canvas.drawString(2.75 * inch, y_coord, event_venue)
        canvas.setFont('Helvetica', 16)
        y_coord -= 30
        canvas.drawString(2.75 * inch, y_coord, 'Do Not Copy or Distribute')
        canvas.restoreState()

    @staticmethod
    def _unpaid_list_header(canvas, doc, event):
        canvas.saveState()
        canvas.drawImage(LOGO_PATH, 0.45 * inch, PAGE_HEIGHT - inch * 0.75,
                         height=0.5 * inch, width=1.875*inch)
        canvas.setLineWidth(2)
        canvas.line(0.45 * inch, PAGE_HEIGHT - inch * 0.8,
                    PAGE_WIDTH - 0.45 * inch, PAGE_HEIGHT - inch * 0.8)
        canvas.setLineWidth(1)
        canvas.line(0.45 * inch, PAGE_HEIGHT - inch * 0.84,
                    PAGE_WIDTH - 0.45 * inch, PAGE_HEIGHT - inch * 0.84)
        canvas.setFont('Helvetica-Bold', 18)
        canvas.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - inch * 1.15,
                                 'UNPAID DELEGATE LIST')
        canvas.line(PAGE_WIDTH / 2 - inch * 1.5, PAGE_HEIGHT - inch * 1.18,
                    PAGE_WIDTH / 2 + inch * 1.5, PAGE_HEIGHT - inch * 1.18)
        style = ParagraphStyle(
            name='textStyle',
            fontName='Helvetica',
            fontSize=11,
            leading=13,
            alignment=TA_LEFT,
        )
        boilerplate = Paragraph(
            'The undersigned acknowledges having attended "<b>' + \
                event.title + \
                '</b>" that ran beginning on ' + \
                event.date_begins.strftime('%-d %B, %Y') + \
                ', and has received all materials and related benefits of ' \
                'said conference.',
            style
        )
        h = boilerplate.wrap(doc.width, inch * 1.5)[1]
        boilerplate.drawOn(canvas, doc.leftMargin, PAGE_HEIGHT - inch * 1.25 - h)

        canvas.restoreState()

    @staticmethod
    def _small_header(canvas, doc, event, report_title):
        canvas.saveState()

        canvas.drawImage(LOGO_PATH, 0.45 * inch, PAGE_HEIGHT - inch * 0.75,
                         height=0.5 * inch, width=1.875*inch)
        canvas.setFont('Helvetica-Bold', 16)
        canvas.drawString(inch * 2.6, PAGE_HEIGHT - inch * 0.42,
                          report_title)
        canvas.setFont('Helvetica', 13)
        canvas.drawString(inch * 2.6, PAGE_HEIGHT - inch * 0.7,
                          str(event.number) + ' - ' + event.title)

        canvas.restoreState()

    def _make_sign_in_label_list(self, reg_detail):
        event_options = self._event.eventoptions_set.all()
        for option in event_options:
            date_diff = (option.enddate - option.startdate).days
            if RegEventOptions(reg=reg_detail, option=option).exists():
                if date_diff > 0:
                    total_lines_for_day = 0
                    for num in range(date_diff):
                        self._label += option.name + ' Day ' + str(num + 1) \
                            + ' Arr:<br/><br/>Dep:<br/><br/><br/>'
                        total_lines_for_day += 2
                    self._line_groups.append(total_lines_for_day)
                else:
                    self._label += option.name + 'Arr:<br/><br/>' + \
                        'Dep:</br><br/><br/>'
                    self._line_groups.append(2)