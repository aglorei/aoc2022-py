[![AoC](https://badgen.net/badge/AoC/2022/blue)](https://adventofcode.com/2022)
[![Python](https://badgen.net/badge/Python/3.11.0+/blue)](https://www.python.org/downloads/)
![Language](https://badgen.net/badge/Language/Python/blue)
[![Template](https://badgen.net/badge/Template/aocd/blue)](https://github.com/wimglenn/advent-of-code-data)

# 🎄 Advent of Code 2022 Python 🎄

## Solutions

<!--SOLUTIONS-->

[![Day](https://badgen.net/badge/01/%E2%98%85%E2%98%85/green)](src/day01)
[![Day](https://badgen.net/badge/02/%E2%98%85%E2%98%85/green)](src/day02)
[![Day](https://badgen.net/badge/03/%E2%98%85%E2%98%85/green)](src/day03)
[![Day](https://badgen.net/badge/04/%E2%98%85%E2%98%85/green)](src/day04)
[![Day](https://badgen.net/badge/05/%E2%98%85%E2%98%85/green)](src/day05)
[![Day](https://badgen.net/badge/06/%E2%98%85%E2%98%85/green)](src/day06)
[![Day](https://badgen.net/badge/07/%E2%98%85%E2%98%85/green)](src/day07)
[![Day](https://badgen.net/badge/08/%E2%98%85%E2%98%85/green)](src/day08)
[![Day](https://badgen.net/badge/09/%E2%98%85%E2%98%85/green)](src/day09)
[![Day](https://badgen.net/badge/10/%E2%98%85%E2%98%85/green)](src/day10)
![Day](https://badgen.net/badge/11/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/12/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/13/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/14/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/15/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/16/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/17/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/18/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/19/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/20/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/21/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/22/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/23/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/24/%E2%98%86%E2%98%86/gray)
![Day](https://badgen.net/badge/25/%E2%98%86%E2%98%86/gray)

<!--/SOLUTIONS-->

_Click a badge to go to the specific day._

---

## Installation

All project dependencies are covered in the [Dockerfile](Dockerfile) definition in the repository root.

### Local

This assumes Docker as a runtime (feel free to use other runtimes). First ensure that Docker is [installed](https://docs.docker.com/get-docker/). From the repository root, build an image and tag appropriately (e.g., `aoc-py:local`):

```sh
docker build --tag aoc-py:local --file Dockerfile .
```

Once [logged in on Advent of Code](https://adventofcode.com/2022/auth/login), locate your session key; this shows up as the value for the `cookie` key in your request headers that you can pull out from browser network tab. Write this value to a `.env` file in the repository root under `AOC_SESSION` variable:

```sh
AOC_SESSION=<insert session key here>
```

From the repository root, instantiate a container with the current directory mounted and environment variables exported:

```sh
docker run --rm -it \
  --env-file .env \
  --volume $PWD:/aoc-py/$(basename $PWD) \
  --workdir /aoc-py/$(basename $PWD) \
  aoc-py:local /bin/bash
```

### GitHub Codespaces

Once [logged in on Advent of Code](https://adventofcode.com/2022/auth/login), locate your session key; this shows up as the value for the `cookie` key in your request headers that you can pull out from browser network tab. Manage this value as an [encrypted secret for your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces) and name it `AOC_SESSION`.

Create a Codespace from your repository fork.

### Develop with aocrunner

After getting setup, whether it's locally or on GitHub Codespaces, create a new subdirectory under `src` for the day of the challenge.

```sh
cp -vr src/template src/day<day>
```

Example:

```sh
cp -vr src/template src/day01
```

Add a `README.md` and use the [`aocd` runner](https://github.com/wimglenn/advent-of-code-data) to write input files as needed. Execute solutions as a library module:

```sh
python -m src.day01.main
```

---

## Results

<!--RESULTS-->

```
Day 01
Time part 1: 0.222ms
Time part 2: 0.231ms
Both parts: 0.452833ms
```

```
Day 02
Time part 1: 1.869ms
Time part 2: 1.008ms
Both parts: 2.876208ms
```

```
Day 03
Time part 1: 0.448ms
Time part 2: 0.358ms
Both parts: 0.806166ms
```

```
Day 04
Time part 1: 5.558ms
Time part 2: 3.829ms
Both parts: 9.3865ms
```

```
Day 05
Time part 1: 0.556ms
Time part 2: 0.560ms
Both parts: 1.116333ms
```

```
Day 06
Time part 1: 0.266ms
Time part 2: 0.951ms
Both parts: 1.217417ms
```

```
Day 07
Time part 1: 0.581ms
Time part 2: 0.557ms
Both parts: 1.137751ms
```

```
Day 08
Time part 1: 36.226ms
Time part 2: 12.697ms
Both parts: 48.922501ms
```

```
Day 09
Time part 1: 14.981ms
Time part 2: 70.882ms
Both parts: 85.863001ms
```

```
Day 10
Time part 1: 0.036ms
Time part 2: 0.054ms
Both parts: 0.090208ms
```

```
Day 11
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 12
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 13
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 14
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 15
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 16
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 17
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 18
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 19
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 20
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 21
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 22
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 23
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 24
Time part 1: -
Time part 2: -
Both parts: -
```

```
Day 25
Time part 1: -
Time part 2: -
Both parts: -
```

```
Total stars: 0/50
Total time: 0ms
```

<!--/RESULTS-->

---

✨🎄🎁🎄🎅🎄🎁🎄✨
