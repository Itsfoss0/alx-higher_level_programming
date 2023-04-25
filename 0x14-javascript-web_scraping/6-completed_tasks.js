#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (!err) {
    const data = JSON.parse(body);
    const completedUsers = {};
    data.forEach((element) => {
      if (element.completed && completedUsers[element.userId] === undefined) {
        completedUsers[element.userId] = 1;
      } else if (element.completed) {
        completedUsers[element.userId] += 1;
      }
    });
    console.log(completedUsers);
  }
});
