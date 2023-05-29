function bigSorting(unsorted) {
    // Write your code here
    if(unsorted.length <= 1){
        return unsorted;
    }
    pivot_index = Math.floor(Math.random() * unsorted.length);
    pivot = unsorted[pivot_index];
    less = unsorted.filter((ele, index) => pivot_index !== index && +ele <= +pivot)
    more = unsorted.filter((ele, index) => pivot_index !== index && +ele > +pivot)
    return [...bigSorting(less), pivot, ...bigSorting(more)]
}