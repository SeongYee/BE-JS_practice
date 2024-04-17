const scores = [100, 90, 80, 70, 60];
// for .. of 문으로 코드 작성

let length = 0;
let sum = 0;

for(let score of scores){
    length += 1;
    sum += score;
}

console.log(length);
console.log(sum);
console.log(sum / length);

// while문으로 코드 작성

while(length > 0){
    console.log(scores[length]);
    length--;
}
