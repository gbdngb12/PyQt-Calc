import sys
from PyQt5.QtWidgets import *
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.answer = ""
        self.operator = ""

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠

        layout_equation = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성

        self.equation = QLineEdit("")
        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        #layout_equation_solution.addRow(label_equation, self.equation)
        #layout_equation_solution.addRow(label_solution, self.solution)
        layout_equation_solution.addRow(self.equation)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        #button_clear = QPushButton("CE")
        #button_c = QPushButton("C")
        button_remainder = QPushButton("%")
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x²")
        button_root = QPushButton("√x")
        button_negative = QPushButton("+/-")



        

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_reciprocal.clicked.connect(lambda state, operation = "1/x": self.button_operation_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "square": self.button_operation_clicked(operation))
        button_root.clicked.connect(lambda state, operation = "root": self.button_operation_clicked(operation))
        button_negative.clicked.connect(lambda state, operation = "neg": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clearall = QPushButton("C")
        button_clear = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clearall.clicked.connect(self.button_clearall_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)


        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_equation.addWidget(button_remainder, 0, 0)
        layout_equation.addWidget(button_clearall, 0, 1)
        layout_equation.addWidget(button_clear, 0, 2)
        layout_equation.addWidget(button_backspace,0, 3)
        layout_equation.addWidget(button_reciprocal, 1, 0)
        layout_equation.addWidget(button_square, 1, 1)
        layout_equation.addWidget(button_root, 1, 2)
        layout_equation.addWidget(button_division, 1, 3)

        layout_number.addWidget(button_product,0,3)
        layout_number.addWidget(button_minus,1,3)
        layout_number.addWidget(button_plus,2,3)
        layout_number.addWidget(button_equal, 3, 3)
        layout_number.addWidget(button_dot, 3, 2)
        layout_number.addWidget(button_negative,3,0)


        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_equation)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)
    
    def button_operation_clicked(self, operation):
        if operation == "neg" :
            saved = self.equation.text()
            self.equation.setText("-" + saved)
            return
        if len(self.operator) == 0 :
            self.operator = operation
            self.answer = self.equation.text()
            self.equation.setText("")
        else :
            if self.operator == '+' :
                self.answer = str(float(self.answer) + float(self.equation.text()))
                self.equation.setText("")
            elif self.operator == '-' :
                self.answer = (str(float(self.answer) - float(self.equation.text())))
                self.equation.setText("")
            elif self.operator == '*' :
                self.answer = (str(float(self.answer) * float(self.equation.text())))
                self.equation.setText("")
            elif self.operator == '/' :
                self.answer = (str(float(self.answer) / float(self.equation.text())))
                self.equation.setText("")
            elif self.operator == '%' :
                self.answer = (str(float(self.answer) % float(self.equation.text())))
                self.equation.setText("")
            elif self.operator == '1/x' :
                self.answer = (str(float(self.answer) ** -1))
                self.equation.setText("")
            elif self.operator == 'square' :
                self.answer = (str(float(self.answer) ** 2))
                self.equation.setText("")
            elif self.operator == 'root' :
                self.answer = (str(math.sqrt(float(self.answer))))
                self.equation.setText("")
            self.operator = operation
    def button_equal_clicked(self):
        if self.operator == '+' :
            self.equation.setText(str(float(self.answer) + float(self.equation.text())))
        elif self.operator == '-' :
            self.equation.setText(str(float(self.answer) - float(self.equation.text())))
        elif self.operator == '*' :
            self.equation.setText(str(float(self.answer) * float(self.equation.text())))
        elif self.operator == '/' :
            self.equation.setText(str(float(self.answer) / float(self.equation.text())))
        elif self.operator == '%' :
            self.equation.setText(str(float(self.answer) % float(self.equation.text())))
        elif self.operator == '1/x' :
            self.equation.setText(str(float(self.answer) ** -1))
        elif self.operator == 'square' :
            self.equation.setText(str(float(self.answer) ** 2))
        elif self.operator == 'root' :
            self.equation.setText(str(math.sqrt(float(self.answer))))
        self.operator = ''

    def button_clear_clicked(self) :
        self.equation.setText("")
    def button_clearall_clicked(self):
        self.answer = ""
        self.operator = ""
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
