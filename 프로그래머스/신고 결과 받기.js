const id_list1 = ["muzi", "frodo", "apeach", "neo"];
const report1 = [
  "muzi frodo",
  "apeach frodo",
  "frodo neo",
  "muzi neo",
  "apeach muzi",
];
const k1 = 2;

function solution(id_list, report, k) {
  let result = Array(id_list.length).fill(0);
  let reportList = {};

  id_list.map((user) => {
    reportList[user] = [];
  });

  report.map((summary) => {
    const [userId, reportId] = summary.split(" ");

    if (!reportList[reportId].includes(userId)) {
      reportList[reportId].push(userId);
    }
  });

  for (const key in reportList) {
    if (reportList[key].length >= k) {
      reportList[key].map((user) => {
        result[id_list.indexOf(user)] += 1;
      });
    }
  }

  return result;
}

console.log(solution(id_list1, report1, k1));
