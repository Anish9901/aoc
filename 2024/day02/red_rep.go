// problem: https://adventofcode.com/2024/day/2
// input: https://adventofcode.com/2024/day/2/input

package day02

import (
	"fmt"
	"os"
	"strconv"
	s "strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func solve_p1(input_ints []int) int {
	check_safe := 0
	if len(input_ints) >= 2 {
		if input_ints[0] < input_ints[1] {
			//check increasing
			counter := 0
			for i := range len(input_ints) {
				if i+1 <= len(input_ints) - 1 && input_ints[i] < input_ints[i+1] {
					if input_ints[i+1] - input_ints[i] <= 3 {
						counter++
					}
				}
				if counter == len(input_ints) - 1 {
					check_safe = 1
				}
			}
		} else if input_ints[0] > input_ints[1] {
			// check decreasing
			counter := 0
			for i := range len(input_ints) {
				if i+1 <= len(input_ints) - 1 && input_ints[i] > input_ints[i+1] {
					if input_ints[i] - input_ints[i+1] <= 3 {
						counter++
					}
				}
				if counter == len(input_ints) - 1 {
					check_safe = 1
				}
			}
		} else {
			// do nothing
		}
	}
	return check_safe
}


func solve_p2(input_ints []int) int {
	check_safe := 0
	// fmt.Println(input_ints)
	for i := range len(input_ints) {
		input := make([]int, len(input_ints))
		copy(input, input_ints)
		// remove one element at a time and check if it is safe
		if i == len(input_ints) - 1 {
			// fmt.Println(input_ints[:i])
			check_safe = solve_p1(input_ints[:i])
		} else {
			// fmt.Println(append(input_ints[:i], input_ints[i+1:]...))
			check_safe = solve_p1(append(input_ints[:i], input_ints[i+1:]...))
		}
		if check_safe == 1 {
			return check_safe
		}
		input_ints = input
	}
	return check_safe
}

func Run() {
	dat, err := os.ReadFile("day02/red_rep_input.txt")
	check(err)
	raw_input := s.Split(string(dat), "\n")
	safe_counter_p1 := 0
	safe_counter_p2 := 0
	for i := range len(raw_input) {
		input_strings := s.Split(raw_input[i], " ")
		input_ints := make([]int, len(input_strings))
		for j, inp := range input_strings {
			num, _ := strconv.Atoi(inp)
			input_ints[j] = num
		}
		// fmt.Println(input_ints)
		safe_counter_p1 += solve_p1(input_ints)
		if solve_p1(input_ints) != 1 {
			safe_counter_p2 += solve_p2(input_ints)
		}
	}
	fmt.Println(safe_counter_p1)
	fmt.Println(safe_counter_p1 + safe_counter_p2)
}
