/**
 * @param {number[]} nums
 * @return {number[]}
 */
const smallerNumbersThanCurrent = function(nums) {
    const sortedNums = quickSort(nums);
    return nums.map((ele, indx, arr) => {
        const lastIndx = sortedNums.indexOf(ele)
        return arr.slice(0, lastIndx).length
    })
        
};

const quickSort = (arr) => {
    if(arr.length <= 1){
        return arr
    }
    const pivot_index = Math.floor(Math.random()*arr.length);
    const pivot = arr[pivot_index];
    const arr_less = arr.filter((ele, indx) => ele <= pivot && indx !== pivot_index);
    const arr_more = arr.filter((ele, indx) => ele > pivot && indx !== pivot_index);
    return [...quickSort(arr_less), pivot, ...quickSort(arr_more)];
}