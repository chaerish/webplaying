const getCalendar = (weekDate) => {
    const currentYear = new Date(weekDate).getFullYear();
    const currentMonth = new Date(weekDate).getMonth() + 1;
    const currentDay = new Date(weekDate).getDate();

    document.querySelector(`.year-mon`).innerText = `${currentYear} ${currentMonth}월`;

    let htmlDummy = '';
    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay}</p>`;
    document.querySelector(`.rec2`).innerHTML = htmlDummy;

    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay+1}</p>`;
    document.querySelector(`.rec3`).innerHTML = htmlDummy;

    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay+2}</p>`;
    document.querySelector(`.rec4`).innerHTML = htmlDummy;

    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay+3}</p>`;
    document.querySelector(`.rec5`).innerHTML = htmlDummy;

    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay+4}</p>`;
    document.querySelector(`.rec6`).innerHTML = htmlDummy;

    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay+5}</p>`;
    document.querySelector(`.rec7`).innerHTML = htmlDummy;

    htmlDummy = `<p class="week-day">${currentMonth}/${currentDay+6}</p>`;
    document.querySelector(`.rec8`).innerHTML = htmlDummy;

}

const weekDate = new Date();
getCalendar(weekDate);


// 미니 캘린더 프리뷰
let sideDate = new Date();

const createCalendar = () => {

    const viewYear = sideDate.getFullYear(); // 해당 년 받아오기
    const viewMonth = sideDate.getMonth(); // 해당 월 받아오기

    var monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]; // 달 이름을 영어로 출력하기 위한 배열

    document.querySelector(".week-year-month").textContent = `${monthNames[viewMonth]}`;

    const prevLast = new Date(viewYear, viewMonth, 0); // 지난달의 마지막 날 Date 객체
    const thisLast = new Date(viewYear, viewMonth + 1, 0); // 이번달의 마지막 날 Date 객체

    const PLDate = prevLast.getDate(); // 지난달의 마지막 날짜
    const PLDay = prevLast.getDay(); // 지난달의 마지막 요일

    const TLDate = thisLast.getDate(); // 이번달의 마지막 날짜
    const TLDay = thisLast.getDay(); // 이번달의 마지막 요일

    // 날짜들을 담아둘 배열
    const prevDates = []; // 이전달 날짜
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = []; // 다음달 날짜

    if (PLDay !== 6) { // 이전 달을 표현할 날짜 생성 (지난달 마지막 요일이 토요일(6) 이면 굳이 그릴 그릴 필요 없음)
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

        for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i); // 이번달 마지막 날짜의 요일을 기준으로 필요한 개수를 파악해서 1부터 1씩 증가시키며 하나씩 채워넣음
    }

    // push() => 배열의 끝에 하나 이상의 요소를 추가하고 배열의 새로운 길이 반환
    const dates = prevDates.concat(thisDates, nextDates); // concat 메서드를 통해서 세 배열을 합침
    const firstDateIndex = dates.indexOf(1); // 지난달 부분을 알아내기 위함
    const lastDateIndex = dates.lastIndexOf(TLDate); // 다음달 부분을 알아내기 위함

    dates.forEach((date, i) => { // 이전달과 다음달 부분의 투명도 조절 위함
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 ?
            'this' // 이번달
            :
            'other'; // 나머지 (span대그로 감싸 classa 로 지정)
        dates[i] = `<button class="week-date"><span class="${condition}">${date}</span></button>`;
    })

    document.querySelector('.week-dates').innerHTML = dates.join('');

    const weekToday = new Date(); // 오늘 날짜 표기하기 위해
    if (viewMonth === weekToday.getMonth() && viewYear === weekToday.getFullYear()) { // 현재 월을 보고 있는게 맞는지
        for (let sideDate of document.querySelectorAll('.this')) { // this 태그 찾기
            if (+sideDate.innerText === weekToday.getDate()) { // +연산자로 숫자로 변경
                sideDate.classList.add('weekToday'); // 해당 태그에 today 클래스 추가
                break;
            }
        }
    }
}

createCalendar();

const goWeekToday = () => {
    sideDate = new Date();
    createCalendar();
}