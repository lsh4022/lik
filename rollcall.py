<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>课堂点名系统</title>
    <style>
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            text-align: center;
        }
        #display {
            font-size: 48px;
            margin: 30px 0;
            padding: 20px;
            border: 3px solid #007bff;
            border-radius: 10px;
            min-height: 100px;
        }
        .highlight {
            color: #dc3545;
            font-weight: bold;
            background-color: #ffeeba;
            padding: 5px 10px;
            border-radius: 5px;
        }
        .input-group {
            margin: 20px 0;
        }
        input[type="text"] {
            padding: 8px;
            width: 300px;
            margin-right: 10px;
        }
        button {
            padding: 10px 20px;
            margin: 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }
        #startBtn {
            background-color: #28a745;
            color: white;
        }
        #stopBtn {
            background-color: #dc3545;
            color: white;
        }
        #addBtn {
            background-color: #007bff;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="input-group">
            <input type="text" id="studentName" placeholder="输入学生姓名">
            <button id="addBtn" onclick="addStudent()">添加学生</button>
        </div>
        
        <div id="display">准备就绪</div>
        
        <button id="startBtn" onclick="startRoll()">开始点名</button>
        <button id="stopBtn" onclick="stopRoll()" disabled>停止</button>
    </div>

    <script>
        let students = [];
        let intervalId = null;
        const display = document.getElementById('display');
        const startBtn = document.getElementById('startBtn');
        const stopBtn = document.getElementById('stopBtn');

        function addStudent() {
            const nameInput = document.getElementById('studentName');
            const name = nameInput.value.trim();
            
            if (name) {
                students.push(name);
                nameInput.value = '';
                nameInput.focus();
            }
        }

        function startRoll() {
            if (students.length === 0) {
                alert('请先添加学生姓名！');
                return;
            }

            startBtn.disabled = true;
            stopBtn.disabled = false;
            display.classList.remove('highlight');

            intervalId = setInterval(() => {
                const randomIndex = Math.floor(Math.random() * students.length);
                display.textContent = students[randomIndex];
            }, 100);
        }

        function stopRoll() {
            clearInterval(intervalId);
            startBtn.disabled = false;
            stopBtn.disabled = true;
            display.classList.add('highlight');
        }
    </script>
</body>
</html>
