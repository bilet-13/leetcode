func hIndex(citations []int) int {
    sort.Ints(citations)

    for i:= len(citations)-1; i > -1; i--{
        if len(citations) - i == citations[i]{
            return len(citations) - i
        }
        if len(citations) - i > citations[i]{
            return len(citations) - i - 1
        }
    }

    return len(citations)
}