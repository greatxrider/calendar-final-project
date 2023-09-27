# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalendarFinal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

#Creators : Jeph Mari Daligdig
#           Abdul Jalil Marangit
#Topic      Calendar
#Date       May 25, 2019 

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 496)

        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 811, 321))
        self.calendarWidget.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2019, 12, 31))
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 340, 201, 16))
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 370, 771, 41))
        self.textBrowser.setObjectName("textBrowser")

        self.Comments = QtWidgets.QTextBrowser(Form)
        self.Comments.setGeometry(QtCore.QRect(20, 450, 256, 31))
        self.Comments.setObjectName("Comments")

        self.CommentsLabel = QtWidgets.QLabel(Form)
        self.CommentsLabel.setGeometry(QtCore.QRect(20, 420, 71, 16))
        self.CommentsLabel.setObjectName("CommentsLabel")

        # Our Own Initialization

        self.calendarWidget.clicked[QtCore.QDate].connect(self.ShowSelectedDate)
        self.calendarWidget.clicked[QtCore.QDate].connect(self.ShowHoliday)
        date = self.calendarWidget.selectedDate()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Calendar for 2019", "Calendar for 2019"))
        self.CommentsLabel.setText("Comments")

        # Our Own Functions

    def ShowSelectedDate(self, date):
        self.label.setText(date.toString())
        
    def ShowHoliday(self, date):
        import datetime
        
        Holidays = {'New Years Day': datetime.date(2019,1,1), 'New Years Holiday': datetime.date(2019,1,2),
        'Chinese New Year': datetime.date(2019,2,5), 'People Power Revolution': datetime.date(2019,2,25), 'Davao City Day': datetime.date(2019,3,16), 
        'The Day of Valor': datetime.date(2019,4,9), 'Maundy Thursday':datetime.date(2019,4,18), 'Good Friday': datetime.date(2019,4,19), 
        'Black Saturday': datetime.date(2019,4,20), 'Labor Day': datetime.date(2019,5,1), 'Public Holiday': datetime.date(2019,5,13), 
        'Eidl Fitr': datetime.date(2019,6,5),'Independence Day': datetime.date(2019,6,12), 'Manila Day': datetime.date(2019,6,24), 
        'Eidul Adha': datetime.date(2019,8,12), 'Ninoy Aquino Day': datetime.date(2019,8,21), 'National Heroes Day': datetime.date(2019,8,26), 
        'All Saints Day': datetime.date(2019,11,1), 'All Souls Day': datetime.date(2019,11,2), 'Bonifacio Day': datetime.date(2019,11,30),
        'Immaculate Conception Day': datetime.date(2019,12,8), 'Christmas Eve': datetime.date(2019,12,24), 'Christmas Day': datetime.date(2019,12,25),
        'Rizal Day': datetime.date(2019,12,30),'New Years Eve': datetime.date(2019,12,31) }



        if self.calendarWidget.selectedDate() != Holidays:
            self.textBrowser.setText("No Holiday")
            self.Comments.setText("None")

        if self.calendarWidget.selectedDate() == Holidays['New Years Day']:
            self.textBrowser.setText("New Years Day")
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['New Years Holiday']:
            self.textBrowser.setText("New Years Holiday")
            self.Comments.setText("Governments, Universities and Colleges")

        if self.calendarWidget.selectedDate() == Holidays['Chinese New Year']:
            self.textBrowser.setText('Chinese New Year')
            self.Comments.setText('Special Non-working day')

        if self.calendarWidget.selectedDate() == Holidays['People Power Revolution']:
            self.textBrowser.setText('People Power Revolution')
            self.Comments.setText("Special Non-working day")

        if self.calendarWidget.selectedDate() == Holidays['Davao City Day']:
            self.textBrowser.setText('Davao City Day')
            self.Comments.setText("Davao City only. Marks the creation of the city")

        if self.calendarWidget.selectedDate() == Holidays['The Day of Valor']:
            self.textBrowser.setText('The Day of Valor')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Maundy Thursday']:
            self.textBrowser.setText('Maundy Thursday')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Good Friday']:
            self.textBrowser.setText('Good Friday')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Black Saturday']:
            self.textBrowser.setText('Black Saturday')
            self.Comments.setText("Special Non-working day")

        if self.calendarWidget.selectedDate() == Holidays['Labor Day']:
            self.textBrowser.setText('Labor Day')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Public Holiday']:
            self.textBrowser.setText('Public Holiday')
            self.Comments.setText("Special Non-working day for elections")

        if self.calendarWidget.selectedDate() == Holidays['Eidl Fitr']:
            self.textBrowser.setText('Eidl Fitr')
            self.Comments.setText("The Feast of Ramadan. Date to be confirmed")

        if self.calendarWidget.selectedDate() == Holidays['Independence Day']:
            self.textBrowser.setText('Independence Day')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Manila Day']:
            self.textBrowser.setText('Manila Day')
            self.Comments.setText("Manila only. Marks the foundation of the city")

        if self.calendarWidget.selectedDate() == Holidays['Eidul Adha']:
            self.textBrowser.setText('Eidul Adha')
            self.Comments.setText("Sacrificed Feast. Date to be confirmed.")

        if self.calendarWidget.selectedDate() == Holidays['Ninoy Aquino Day']:
            self.textBrowser.setText('Ninoy Aquino Day')
            self.Comments.setText("Special non-working day")

        if self.calendarWidget.selectedDate() == Holidays['National Heroes Day']:
            self.textBrowser.setText('National Heroes Day')
            self.Comments.setText("Regular holiday. Last Monday of August")

        if self.calendarWidget.selectedDate() == Holidays['All Saints Day']:
            self.textBrowser.setText('All Saints Day')
            self.Comments.setText("Special Non-working day")

        if self.calendarWidget.selectedDate() == Holidays['All Souls Day']:
            self.textBrowser.setText('All Souls Day')
            self.Comments.setText("Additional Special Non-working day")

        if self.calendarWidget.selectedDate() == Holidays['Bonifacio Day']:
            self.textBrowser.setText('Bonifacio Day')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Immaculate Conception Day']:
            self.textBrowser.setText('Immaculate Conception Day')
            self.Comments.setText('Special Non-working holiday from 2018')

        if self.calendarWidget.selectedDate() == Holidays['Christmas Eve']:
            self.textBrowser.setText('Christmas Eve')
            self.Comments.setText("Additional Special Non-working day")

        if self.calendarWidget.selectedDate() == Holidays['Christmas Day']:
            self.textBrowser.setText('Christmas Day')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['Rizal Day']:
            self.textBrowser.setText('Rizal Day')
            self.Comments.setText("Regular Holiday")

        if self.calendarWidget.selectedDate() == Holidays['New Years Eve']:
            self.textBrowser.setText('New Years Eve')
            self.Comments.setText("Special Non-working day")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

