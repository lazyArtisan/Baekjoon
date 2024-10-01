# [Gold V] WINDOWS - 3255 

[문제 링크](https://www.acmicpc.net/problem/3255) 

### 성능 요약

메모리: 109240 KB, 시간: 92 ms

### 분류

기하학, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 10월 1일 11:41:34

### 문제 설명

<p>In popular operating system we opened lots of windows.</p>

<p>Each window is rectangle consisting of small squares (of dimension 1 x 1).</p>

<p>Newly opened windows, depending of its position and size, can (partially or totally) cover some earlier opened windows.</p>

<p>We can close window with mouse if we click on its upper right small square, which in that moment must be visible. Square of some window is visible if there is no later opened window, which is not yet closed.</p>

<p>Write the program that will calculate the minimal number of mouse clicks to close the window that we opened first.</p>

### 입력 

 <p>In first line of input file there is integer N, number of windows, 1 ≤ N ≤ 100.</p>

<p>In each of the next N lines there are 4 integers R1, S1, R2 and S2, separated with spaces, 1 ≤ R1 ≤ R2 ≤ 10000, 1 ≤ S1 ≤ S2 ≤ 10000. Numbers R1 and S1 stand for row and column of the screen in which is upper-left square of that window, and R2 and S2 stand for row and column of the screen in which is lower-right square of that windows. Windows are opened in the same order like they appears in the input file.</p>

<p>We imagine screen as it consits of rows and columns of small squares. Rows are numerated from the top to the bottom, columns from the left to the right, and upper-left square on the screen is in the first row and first column. </p>

### 출력 

 <p>In first and only line of output file you should write the minimal number of mouse clicks. </p>

