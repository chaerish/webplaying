// 버튼 요소를 선택합니다.
var button = document.getElementById("send_request");

// 버튼 클릭 이벤트에 대한 이벤트 리스너를 추가합니다.
button.addEventListener("click", function () {
    // 버튼의 색을 변경합니다.
    button.style.backgroundColor = "#67BEC7";

    // 버튼의 텍스트를 변경합니다.
    button.textContent = "요청됨";
});
