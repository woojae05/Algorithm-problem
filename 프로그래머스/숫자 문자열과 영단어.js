const s1 = "oneone4seveneight";

function solution(s) {
  const numberList = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  while (true) {
    for (let i = 0; i < numberList.length; i++) {
      s = s.replace(numberList[i], "" + i);
    }
    if (+s > 1) {
      break;
    }
  }

  return Number(s);
}

// 깔끔한 코드
// function solution(s) {
//   let numbers = [
//     "zero",
//     "one",
//     "two",
//     "three",
//     "four",
//     "five",
//     "six",
//     "seven",
//     "eight",
//     "nine",
//   ];
//   var answer = s;

//   for (let i = 0; i < numbers.length; i++) {
//     let arr = answer.split(numbers[i]);
//     answer = arr.join(i);
//   }

//   return Number(answer);
// }

console.log(solution(s1));
