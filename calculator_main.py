import sys
from PyQt5.QtWidgets import *
import math
import numpy

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.answer = ""
        self.operator = ""

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QHBoxLayout()
        layout_operation2 = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
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



        

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_reciprocal.clicked.connect(lambda state, operation = "1/x": self.button_operation_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "square": self.button_operation_clicked(operation))
        button_root.clicked.connect(lambda state, operation = "root": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)
        

        layout_operation2.addWidget(button_remainder)
        layout_operation2.addWidget(button_reciprocal)
        layout_operation2.addWidget(button_square)
        layout_operation2.addWidget(button_root)
        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

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
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_operation2)
        main_layout.addLayout(layout_clear_equal)
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
        #self.answer = self.equation.text()
        self.operator = operation
        self.answer = self.equation.text()
        self.equation.setText("")

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
            self.equation.setText(str(float(self.answer) / float(self.equation.text())))
        elif self.operator == 'square' :
            self.equation.setText(str(float(self.answer) ** float(self.equation.text())))
        elif self.operator == 'root' :
            self.equation.setText(str(math.sqrt(float(self.answer))))


    def button_clear_clicked(self):
        self.answer = ""
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
