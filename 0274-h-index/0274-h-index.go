func hIndex(citations []int) int {
    sort.Ints(citations)

    for i:= len(citations)-1; i > -1; i--{
        num_paper := len(citations) - i
        if num_paper == citations[i]{
            return num_paper
        }
        if num_paper > citations[i]{
            return num_paper - 1
        }
    }

    return len(citations)
}