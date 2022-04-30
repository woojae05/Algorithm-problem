const numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
const hand1 = "right";

function solution(numbers, hand) {
  var answer = "";
  var left = 10;
  var right = 12;

  for (let i = 0; i < numbers.length; i++) {
    numbers[i] == 0 ? (numbers[i] = 11) : numbers1[i];
    if (numbers[i] % 3 == 1) {
      answer += "L";
      left = numbers[i];
    } else if (numbers[i] % 3 == 0) {
      answer += "R";
      right = numbers[i];
    } else {
      if (findDistance(left, numbers[i]) < findDistance(right, numbers[i])) {
        answer += "L";
        left = numbers[i];
      } else if (
        findDistance(left, numbers[i]) > findDistance(right, numbers[i])
      ) {
        answer += "R";
        right = numbers[i];
      } else {
        if (hand == "right") {
          answer += "R";
          right = numbers[i];
        } else {
          answer += "L";
          left = numbers[i];
        }
      }
    }
  }
  return answer;
}

function getX(number) {
  return (number - 1) % 3;
}

function getY(number) {
  return Math.floor((number - 1) / 3);
}

function findDistance(number1, number2) {
  let diffX = Math.abs(getX(number1) - getX(number2));
  let diffY = Math.abs(getY(number1) - getY(number2));
  return diffX + diffY;
}

console.log(solution(numbers1, hand1));
