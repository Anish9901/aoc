package day03

import (
	"fmt"
	"os"
	"strconv"
	"regexp"
	s "strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func solve_p1(input string) int {
	result := 0
	r, _ := regexp.Compile(`mul\([0-9]{1,3},[0-9]{1,3}\)`)
	all_mul_matches := r.FindAllString(input, -1)
	r1, _ := regexp.Compile(`[0-9]{1,3},[0-9]{1,3}`)
	for i := range len(all_mul_matches) {
		a := s.Split(r1.FindAllString(all_mul_matches[i], -1)[0], ",")
		first, _ := strconv.Atoi(a[0])
		second, _ := strconv.Atoi(a[1])
		result += first * second
	}
	return result
}

func solve_p2(input string) int {
	do := true
	var all_valid_mul_matches []string
	result := 0
	r, _ := regexp.Compile(`do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)`)
	all_mul_do_dont_matches := r.FindAllString(input, -1)
	// fmt.Println(all_mul_do_dont_matches)
	for i := range len(all_mul_do_dont_matches) {
		if all_mul_do_dont_matches[i] == "don't()" {
			do = false
		} else if all_mul_do_dont_matches[i] == "do()" {
			do = true
		}
		if do && all_mul_do_dont_matches[i] != "do()"{
			all_valid_mul_matches = append(all_valid_mul_matches, all_mul_do_dont_matches[i])
		}
	}
	r1, _ := regexp.Compile(`[0-9]{1,3},[0-9]{1,3}`)
	for i := range len(all_valid_mul_matches) {
		a := s.Split(r1.FindAllString(all_valid_mul_matches[i], -1)[0], ",")
		// fmt.Println(a)
		first, _ := strconv.Atoi(a[0])
		second, _ := strconv.Atoi(a[1])
		result += first * second
	}
	return result
}

func Run() {
	dat, err := os.ReadFile("day03/mul_ove_input.txt")
	check(err)
	raw_input := s.Split(string(dat), "\n")
	mul_result_p1 := 0
	mul_result_p2 := 0
	for j := range len(raw_input) {
		mul_result_p1 += solve_p1(raw_input[j])
		mul_result_p2 += solve_p2(raw_input[j])
	}
	// input := "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
	fmt.Println(mul_result_p1)
	fmt.Println(mul_result_p2)
}
