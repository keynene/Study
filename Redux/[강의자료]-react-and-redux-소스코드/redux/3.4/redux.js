/* 
	createStore
	각종의 state들을 담고 있는 state 저장소
	return값으로 여러 state를 반환할 것임

	worker(reducer)
	상태를 원본 변화 없이 바꾸기만 하려면  store함수 "밖"에서 변경해줘야 함

	send(dispatch)
	worker를 통해 바뀐 state값을 createStore 밖으로 "전달"해줌 

	getState
	createStore안에 있는 state를 반환해주는 함수 (가져다 쓰기 위해)
	dispatch는 state를 변경하기만 하니까 반환해주는 getState함수도 필요함

	구독발행모델
	컴포넌트가 무수히 많은 프로젝트에서 하나의 컴포넌트가 변경되면
	다른 컴포넌트들은 해당 컴포넌트가 변경되었다는 사실을 알 수가 없으므로
	해당 컴포넌트를 구독해놓고, 변경될 때마다 발행을 요청하는 모델
	(여러개의 컴포넌트들을 구독해놓고, 이벤트 발생할 때마다 바뀐 컴포넌트들을 반환)

  actionCreator
  매번 action-type을 넘길 떄마다 "type:어쩌고", "type:어쩌고" ...
  반복하기 귀찮으니 타입자체를 반환해버리는 함수
  payload도 함께 전달함
*/


// export function actionCreator(type, payload) {
//   return {
//     type,
//     payload,
//   }
// }

//Currying 이용해서 위 함수를 redux스럽게 개선
//함수의 인자가 여러 개 있을 때 각각의 인자를 할당하는 여러 개의 내부 함수로 쪼갬
export const actionCreator = type => payload => ({
  type,
  payload,
});



export function createStore(reducer) {
	let state;
	let handlers = []; //구독함수들을 저장

	function dispatch(action) { //3:상태를 원본 변화없이 전달만 하는 함수인 dispatch 호출 
		state = reducer(state, action); //4:dispatch를 통해 상태를 바꾸는 함수인 reducer 호출
		handlers.forEach(handler => handler()); //데이터가 바뀔 때마다 구독기 호출
	}

	function subscribe(handler) { 
		//구독기 : handlers에 함수를 등록, 인자로 함수를 받음(handler)
		handlers.push(handler)
	}

	function getState() {
		return state;
	}

	return { //store밖에서 호출할 함수들을 return
		dispatch, //6:reducer 통해 바꾼 state를 store함수에 return
		getState,
		subscribe,
	};
}