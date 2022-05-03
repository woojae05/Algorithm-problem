const participant1 = ["mislav", "stanko", "mislav", "ana"];
const completion1 = ["stanko", "ana", "mislav"];

function solution(participant, completion) {
  let answer;
  participant = participant.sort();
  completion = completion.sort();
  let str = (participant = participant.join(""));
  for (let i = 0; i < completion.lenght; i++) {
    str = str.replace(completion[i], "");
  }
  console.log(str);

  return answer;
}

console.log(solution(participant1, completion1));
