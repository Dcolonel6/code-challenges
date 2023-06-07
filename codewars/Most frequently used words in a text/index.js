function topThreeWords(text) {
    const registry = {}
    const aryWords = text.split(" ")
    let mostUsend, secondMostUsed, thirdMostUsed = ""
    for(const word of aryWords){
        registry[word]  = registry[word] ? registry[word] + 1 : 1
    }
    return quickSort(Object.entries(registry)).slice(0,3).map(([key]) => key)   
}

function quickSort(arr){
  
    if(arr.length < 2) return arr
    const pivot_index = Math.floor(Math.random() * arr.length)
    const [pivot_key, pivot_value] = arr[pivot_index]
    const leftAry = arr.filter(([key, value], index) => index !== pivot_index && value <= pivot_value)
    const rightAry = arr.filter(([key, value], index) => index !== pivot_index && value > pivot_value)

    return [
        ...quickSort(rightAry) ,
        arr[pivot_index],
        ...quickSort(leftAry)
               
    ]
}
console.log(
    topThreeWords(`In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.`)
)

