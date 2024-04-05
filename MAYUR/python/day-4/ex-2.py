
# Ex-4.2
# Create a function/input that counts the integer's number of digits.
# Solve this without using strings.

# Example :
# 	count(318) ➞ 3
# 	count(-92563) ➞ 5
# 	count(4666) ➞ 4
# 	count(-314890) ➞ 6
# 	count(654321) ➞ 6
# 	count(638476) ➞ 6


constcount = (n) =>{
  let a = n;
  if (n < 0) {
    a = -(n)
  }
  let b = 0;
  for (let i = 0; a > 1; i++) {
    a = a / 10;
    b += 1;
    console.log("i : " + i);
  }
return b;
};

console.log(count(318));
console.log(count(-92563));
console.log(count(4666));
console.log(count(-314890));
console.log(count(654321));
console.log(count(638476));