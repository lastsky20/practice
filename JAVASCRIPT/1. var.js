// let : 변할 수 있는 값, 
// 문자열 변수
let name1 = "mike";  
let name2= 'm\'ike';   // \ 역슬래시 사용시 특수문자로 인식
let name3 = `my name is ${name1}`;  // 문자열 내부에 변수를 삽입시
var name4 = "string"

// //const : 상수, 변하지 않는 값, 대문자로 표기
const AGE = 30;
console.log(name4)
console.log(name3)
console.log(name1 + " " + name2 + name3)

//1 + 1 , 10 - 1 , 3 * 2 , 6 / 3, 5 % 3
// ==, >, <, <=, >=, !=

// 논리형
const a = true;
const b = false;

// null, undefined
const user = null;
//const user2; // undefined

// typeof
const type1 = "string";
const type2 = 1234;

console.log(typeof type1);
console.log(typeof type2);



