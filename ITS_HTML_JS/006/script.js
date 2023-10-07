// if else

//if(2 > 0){
//    alert("2 > 0");
//}else{
//    alert("2 < 0");
//}

// >; <; >=; <=; ==; !=;

//let number = 10;
//
//if (number > 0) {
//    alert("number +");
//} else {
//    alert("number -");
//}
//
//let userAnswer = 4;
//if (userAnswer == 4) {
//    alert("yes")
//} else {
//    alert("No");
//}
//
//const year = 2023;
//let userAge = +prompt("Введите год рождения: ");
//let calk = year - userAge;
//if (calk >= 18){
//    alert("Вы совершеннлетний человек!");
//}else {
//    alert("Сорри, вам нет 18")
//};
//let age = 20;
//
//if (age > 0 && age < 120) {
//    if (age < 6) {
//        alert("Baby");
//    } else if (age < 17) {
//        alert("Child");
//    } else if (age < 23) {
//        alert("Student");
//    } else {
//        alert("Worker");
//    }
//} else {
//    alert("Wrong data");
//}

// && - и || - или

//let ans = prompt("admin");
//
//if (ans == "admin" || ans == "Admin") {
//    
//    alert("Correct!")
//    
//} else {
//    alert("Wrong")
//}


// switch
//let x = 4;
//
//switch(x){
//    case 1:
//        alert("1");
//        break;
//    case 2:
//        alert("2")
//        break;
//    case 3:
//        alert("3")
//        break;
//    default:
//        alert("No data")
//}

//let month = +prompt("Введите номер месяца");
//
//switch (month) {
//    case 1:
//        alert("January");
//        break;
//    case 2:
//        alert("February");
//        break;
//    case 3:
//        alert("March");
//        break;
//    case 4:
//        alert("April");
//        break;
//    case 5:
//        alert("May");
//        break;
//    case 6:
//        alert("June");
//        break;
//    case 7:
//        alert("July");
//        break;
//    case 8:
//        alert("August");
//        break;
//    case 9:
//        alert("September");
//        break;
//    case 10:
//        alert("October");
//        break;
//    case 11:
//        alert("November");
//        break;
//    case 12:
//        alert("December");
//        break;
//    default:
//        alert("Неверный номер месяца");
//        break;
//}

//let num1 = +prompt("Введите первое число 1:");
//let num2 = +prompt("Введите второе число 2:");
//let operator = prompt("Введите знак операции (+, -, *, /):");
//
//let result;
//
//switch (operator) {
//    case "+":
//        result = num1 + num2;
//        break;
//    case "-":
//        result = num1 - num2;
//        break;
//    case "*":
//        result = num1 * num2;
//        break;
//    case "/":
//        if (num2 != 0) {
//            result = num1 / num2;
//        } else {
//            alert("Ошибка: деление на ноль!");
//        }
//        break;
//    default:
//        alert("Неверный знак операции!");
//        break;
//}
//
//if (result !== undefined) {
//    alert(result);
//}else {
//    alert("Другая ошибка")
//}

// Тернарный оператор?
// Условие ? Выбражение1 (если да) : Выражение2 (Если нет)

//let num = 1;
//
//let result = num > 0 ? true : false;
//alert(result)
//
//num > 0 ? console.log("true") : console.log("false")

//let num1 = +prompt("Число 1:")
//let num2 = +prompt("Число 2:")
//num1 > num2 ? alert(num1) : alert(num2)

let num = +prompt("Проверка кратности 5")
num % 5 ? alert("Число не кратно 5") : alert("Число кратно 5")
























