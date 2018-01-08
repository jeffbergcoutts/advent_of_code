var fs = require('fs')
var file = '/Users/bergcoutts/Projects/advent_of_code_2017/input_dec1.txt'
var contents = undefined
var number = ""

fs.readFile(file, function (err, contents) {
  number = contents.toString()
//  totalNumbers(number)
  solutionB(number)
})

function totalNumbers(number) {
  var lastNumber = 0
  var totalNumber = 0

  for (var i = 0, len = (number.length - 1); i < len; i += 1) {
    var n = parseInt(number.charAt(i), 10)
    if (lastNumber != 0) {
      if (lastNumber === n) {
        totalNumber = totalNumber + n
      }
    }
    lastNumber = n
  }

  if (lastNumber === parseInt(number.charAt(0))) {
    totalNumber = totalNumber + n
  }

  console.log(totalNumber)
}

function solutionB(number) {
  var length = (number.length - 1)
  var halfway = (length/2)
  var totalNumber = 0

  for (var i = 0; i < length; i += 1) {
    var n = parseInt(number.charAt(i))
    if ((i + halfway) < length) {
      var nHalf = parseInt(number.charAt(i + halfway), 10)
      if (nHalf === n) {
        totalNumber = totalNumber + n
      }
    } else {
      var nHalf = parseInt(number.charAt(i - halfway), 10)
      if (nHalf === n) {
        totalNumber = totalNumber + nHalf
      }
    }
  }

  console.log(totalNumber)
}
