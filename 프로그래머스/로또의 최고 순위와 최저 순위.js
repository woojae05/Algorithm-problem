const loots1 = [44, 1, 0, 0, 31, 25];
const win_nums1 = [31, 10, 45, 1, 6, 19];

function solution(lottos, win_nums) {
  const result = [];
  let cnt = 0;
  let zerro = 0;

  for (let i = 0; i <= win_nums.length; i++) {
    if (lottos[i] == 0) {
      zerro++;
    }
    if (lottos.includes(win_nums[i])) {
      cnt += 1;
    }
  }
  const total = cnt + zerro;
  const high = total < 2 ? 6 : 7 - total;
  const low = cnt < 2 ? 6 : 7 - cnt;

  result.push(high);
  result.push(low);

  return result;
}

console.log(solution(loots1, win_nums1));
