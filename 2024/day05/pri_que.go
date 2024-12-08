package day05

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	s "strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func check_rule(ordering_rule []string, print_input []string) int {
	valid_middle_pg := 0
	for i := range len(print_input) - 1 {
		for j := i + 1; j < len(print_input); j++ {
			//fmt.Println(print_input[j] + "|" + print_input[i])
			if slices.Contains(ordering_rule, print_input[j] + "|" + print_input[i]) {
				//fmt.Println("contains")
				return 0
			}
		}
	}
	valid_middle_pg, _ = strconv.Atoi(print_input[(len(print_input) + 1)/2 - 1])
	return valid_middle_pg
}

func Run() {
	dat, err := os.ReadFile("day05/pri_que_input.txt")
	check(err)
	raw_input := s.Split(string(dat), "\n\n")
	ordering_rule := s.Split(raw_input[0], "\n")
	given_ordering := s.Split(raw_input[1], "\n")
	// fmt.Println(ordering_rule)
	// fmt.Println(given_ordering)
	middle_pg_no := 0
	for i := range len(given_ordering) {
		print_input := s.Split(given_ordering[i], ",")
		// fmt.Println(print_input)
		middle_pg_no += check_rule(ordering_rule, print_input)
		// fmt.Println(check_rule(ordering_rule, print_input))
	}
	fmt.Println(middle_pg_no)
}
