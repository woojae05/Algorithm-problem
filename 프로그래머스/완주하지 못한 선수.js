const participant1 = ["mislav", "stanko", "mislav", "ana"];
const completion1 = ["stanko", "ana", "mislav"];

function solution(participant, completion) {
  participant.sort();
  completion.sort();

  for (let i = 0; i < participant.length; i++) {
    if (participant[i] !== completion[i]) {
      return participant[i];
    }
  }
}
console.log(solution(participant1, completion1));
