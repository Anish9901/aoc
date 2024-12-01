// problem: https://adventofcode.com/2024/day/1
// input: https://adventofcode.com/2024/day/1/input

package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	s "strings"
)

var p = fmt.Println

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func solve_p1(group1 []int, group2 []int) int {
    if len(group1) != len(group2) {
        panic("group1 and group2 should be of same length")
    }
    sort.Ints(group1)
    sort.Ints(group2)
    distance := 0
    for i := range len(group1) {
        if group1[i] >= group2[i] {
            distance += group1[i] - group2[i]
        } else {
            distance += group2[i] - group1[i]
        }
    }
    return distance
}

func solve_p2(group1 []int, group2 []int) int {
    if len(group1) != len(group2) {
        panic("group1 and group2 should be of same length")
    }
    similarity_score := 0
    map_g2 := make(map[int]int)
    for i := range len(group2) {
        map_g2[group2[i]] += 1
    }
    for i := range len(group1) {
        similarity_score += group1[i] * map_g2[group1[i]]
    }
    return similarity_score
}

func main() {
	dat, err := os.ReadFile("../1_his_hys_input.txt")
	check(err)
	raw_input := s.Split(string(dat), "\n")
	var group1 []int
	var group2 []int
	for i := range len(raw_input) {
        input := s.Split(raw_input[i], "   ")
		l, _ := strconv.Atoi(input[0])
		r, _ := strconv.Atoi(input[1])
		group1 = append(group1, l)
		group2 = append(group2, r)
	}
    // Sample input
    // group1 = []int{3, 4, 2, 1, 3, 3}
    // group2 = []int{4, 3, 5, 3, 9, 3}
    fmt.Println(solve_p1(group1, group2)) // 1151792
    fmt.Println(solve_p2(group1, group2)) // 21790168
}
