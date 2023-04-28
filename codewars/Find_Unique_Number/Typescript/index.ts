export function findUniq(arr: number[]): number {
  // Do the magic
  const setUniqueArray: number[] = Array.from(new Set(arr));
  const firstUnique =
    arr[0] === setUniqueArray[0] && arr[arr.length - 1] === setUniqueArray[0];
  if (firstUnique) {
    return setUniqueArray[1];
  } else {
    return arr[arr.length - 1 - 1] === setUniqueArray[0]
      ? arr[arr.length - 1]
      : setUniqueArray[0];
  }
}
