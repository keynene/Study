/*
	actions
	액션들의 type과 payload를 한 번에 전달해주는 actionCreator함수까지는 좋았는데 (redux.js)
	호출 할 때마다 actionCreator이라는 함수를 계속 명시해줘야 하는게 귀찮음
	즉, actions는 "actionCreator(action-type명, payload값)"을 
	한 번에 입력해주는 로직 정도로 보면 됨
*/
import { actionCreator } from './redux.js';
import { INCREASE, DECREASE, RESET } from './action-type.js'

// redux.js의 actionCreator의 함수 구조가 Currying함수로 변경되어서
// actions 내의 함수 전달 방식도 달라짐
//// 쉽게말하면 redux.js의 actionCreator가 "함수"였는데
//// 함수를 담고있는 "변수"로 변경되어서
//// 실제 사용할 떄는 변수명에 파라미터만 전달하면 되게끔 변경됨

// export const increase = () => actionCreator(INCREASE);
export const increase =  actionCreator(INCREASE);
export const decrease =  actionCreator(DECREASE);
export const reset =  actionCreator(RESET);