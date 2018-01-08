var fs = require('fs')
var file = '/Users/bergcoutts/Projects/advent_of_code/2017/input_dec2.txt'
var contents = undefined
var table = ""

fs.readFile(file, function (err, contents) {
  table = contents.toString()
  checkSum(table)
})

function checkSum(table) {
  var str_arr = []
  var str_arr2 = []
  var str_arr = table.split('\n')

  for (var i = 0; i < (str_arr.length - 1); i += 1) {
    str_arr2.push(str_arr[i].split('\t'))
  }

  console.log(str_arr2)
}
