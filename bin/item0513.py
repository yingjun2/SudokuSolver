<!DOCTYPE html>
<html>
<head>
<style>
table {
    border-collapse: collapse;
    border: 1px solid black;
}

th,td {
    border: 1px solid black;
}

table.a {
    table-layout: auto;
    width: 180px;
}

table.b {
    table-layout: auto;
    width: 180px;
}

.wrapper {
    text-align: center;
}

.button {
    position: absolute;
    top: 50%;
}
#solutionButton { display: flex; justify-content: center; }

</style>
</head>
<body>
    {{item.id}}<br>
    {{item.puzzle}}<br>
    {{ item.puzzle.00 }}<br>
    {{ item.puzzle.01 }}<br>
    {{ item.puzzle.02 }}<br>
    {{ item.solution }}<br>
<!--{{item.puzzle}}-->

<!--<p id="demo"></p>-->
<!--<script>-->
<!--var f =  "{{item.puzzle}}"-->
<!--document.getElementById("demo").innerHTML = f[3];-->
<!--</script>-->



<!--<p>{{ item.solution }}</p>-->
<h1 align="center">Welcome to Sudoku Game</h1>

<h2 align="center">sudoku puzzle No. {{ item.id }}</h2>
<table align="center" class="a" border="20" bgcolor="grey">
  <tr bgcolor="lightblue">
    <th>8</th>
    <th>5</th>
    <th> </th>
    <th bgcolor="yellow"> </th>
    <th bgcolor="yellow"> </th>
    <th bgcolor="yellow">2</th>
    <th>4</th>
    <th></th>
    <th></th>
  </tr>
  <tr bgcolor="lightblue">
    <th>7</th>
    <th>2</th>
    <th> </th>
    <th bgcolor="yellow"></th>
    <th bgcolor="yellow"></th>
    <th bgcolor="yellow"> </th>
    <th></th>
    <th> </th>
    <th>9</th>
  </tr bgcolor="yellow">
  <tr bgcolor="lightblue">
    <th></th>
    <th> </th>
    <th>4</th>
    <th bgcolor="yellow"></th>
    <th bgcolor="yellow"> </th>
    <th bgcolor="yellow"></th>
    <th></th>
    <th></th>
    <th> </th>
  </tr>
  <tr bgcolor="yellow">
    <th></th>
    <th> </th>
    <th></th>
    <th bgcolor="lightblue">1</th>
    <th bgcolor="lightblue"> </th>
    <th bgcolor="lightblue">7</th>
    <th></th>
    <th></th>
    <th> </th>
  </tr>
  <tr bgcolor="yellow">
    <th>3</th>
    <th> </th>
    <th>5</th>
    <th bgcolor="lightblue"></th>
    <th bgcolor="lightblue"> </th>
    <th bgcolor="lightblue"></th>
    <th>9</th>
    <th></th>
    <th> </th>
  </tr>
  <tr bgcolor="yellow">
    <th></th>
    <th>4 </th>
    <th></th>
    <th bgcolor="lightblue"></th>
    <th bgcolor="lightblue"> </th>
    <th bgcolor="lightblue"></th>
    <th></th>
    <th></th>
    <th> </th>
  </tr>
  <tr bgcolor="lightblue">
    <th>1</th>
    <th> </th>
    <th>3</th>
    <th bgcolor="yellow">4</th>
    <th bgcolor="yellow"> </th>
    <th bgcolor="yellow">6</th>
    <th>7</th>
    <th>8</th>
    <th> </th>
  </tr>
  <tr bgcolor="lightblue">
    <th></th>
    <th> </th>
    <th></th>
    <th bgcolor="yellow"></th>
    <th bgcolor="yellow">8 </th>
    <th bgcolor="yellow"></th>
    <th></th>
    <th>7</th>
    <th> </th>
  </tr>
  <tr bgcolor="lightblue">
    <th></th>
    <th> </th>
    <th></th>
    <th bgcolor="yellow"></th>
    <th bgcolor="yellow">3 </th>
    <th bgcolor="yellow">6</th>
    <th></th>
    <th></th>
    <th>4</th>
  </tr>
</table>


<p align="center">Click the "Show solution" button to toggle between hiding and showing the solution:</p>

<div class="wrapper">
    <button onclick="myFunction()">Show solution.</button>
</div>


<!--<div class="wrapper">-->
<!--    <button class="button">Button</button>-->
<!--</div>-->


<div id="solutionButton" style="display:none;">
<h2 align="center">sudoku puzzle No. 001 - solution</h2>
<table align="center" class="b">
  <colgroup>
    <col style="background-color: #C0C0C0">
    <col span="2">
  </colgroup>

  <tr bgcolor="lightblue">
    <th>8</th>
    <th>5</th>
    <th>9</th>
    <th bgcolor="yellow">6</th>
    <th bgcolor="yellow">1</th>
    <th bgcolor="yellow">2</th>
    <th>4</th>
    <th>3</th>
    <th>7</th>
  </tr>
  <tr bgcolor="lightblue">
    <th>7</th>
    <th>2</th>
    <th>3</th>
    <th bgcolor="yellow">8</th>
    <th bgcolor="yellow">5</th>
    <th bgcolor="yellow">4</th>
    <th>1</th>
    <th>6</th>
    <th>9</th>
  </tr>
  <tr bgcolor="lightblue">
    <th>1</th>
    <th>6</th>
    <th>4</th>
    <th bgcolor="yellow">3</th>
    <th bgcolor="yellow">7</th>
    <th bgcolor="yellow">9</th>
    <th>5</th>
    <th>2</th>
    <th>8</th>
  </tr>
  <tr bgcolor="yellow">
    <th>9</th>
    <th>8</th>
    <th>6</th>
    <th bgcolor="lightblue">1</th>
    <th bgcolor="lightblue">4</th>
    <th bgcolor="lightblue">7</th>
    <th>3</th>
    <th>5</th>
    <th>2</th>
  </tr>
  <tr bgcolor="yellow">
    <th>3</th>
    <th>7</th>
    <th>5</th>
    <th bgcolor="lightblue">2</th>
    <th bgcolor="lightblue">6</th>
    <th bgcolor="lightblue">8</th>
    <th>9</th>
    <th>1</th>
    <th>4</th>
  </tr>
  <tr bgcolor="yellow">
    <th>2</th>
    <th>4 </th>
    <th>1</th>
    <th bgcolor="lightblue">5</th>
    <th bgcolor="lightblue">9</th>
    <th bgcolor="lightblue">3</th>
    <th>7</th>
    <th>8</th>
    <th>6</th>
  </tr>
  <tr bgcolor="lightblue">
    <th>4</th>
    <th>3</th>
    <th>2</th>
    <th bgcolor="yellow">9</th>
    <th bgcolor="yellow">8</th>
    <th bgcolor="yellow">1</th>
    <th>6</th>
    <th>7</th>
    <th>5</th>
  </tr>
  <tr bgcolor="lightblue">
    <th>6</th>
    <th>1</th>
    <th>7</th>
    <th bgcolor="yellow">4</th>
    <th bgcolor="yellow">2</th>
    <th bgcolor="yellow">5</th>
    <th>8</th>
    <th>9</th>
    <th>3</th>
  </tr>
  <tr bgcolor="lightblue">
    <th>5</th>
    <th>9</th>
    <th>8</th>
    <th bgcolor="yellow">7</th>
    <th bgcolor="yellow">3</th>
    <th bgcolor="yellow">6</th>
    <th>2</th>
    <th>4</th>
    <th>1</th>
  </tr>
</table>
</div>

<script>
function myFunction() {
    var x = document.getElementById("solutionButton");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
</script>


</body>
</html>
