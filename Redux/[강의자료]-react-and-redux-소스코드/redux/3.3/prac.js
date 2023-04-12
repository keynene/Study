/* 
	createStore
	각종의 state들을 담고 있는 state 저장소
	return값으로 여러 state를 반환할 것임

	worker
	상태를 원본 변화 없이 바꾸기만 하려면  store함수 "밖"에서 변경해줘야 함

	send
	worker를 통해 바뀐 state값을 createStore 밖으로 "전달"해줌 

	getState
	createStore안에 있는 state를 반환해주는 함수 (가져다 쓰기 위해)
	send는 state를 변경하기만 하니까 반환해주는 getState함수도 필요함

	구독발행모델
	컴포넌트가 무수히 많은 프로젝트에서 하나의 컴포넌트가 변경되면
	다른 컴포넌트들은 해당 컴포넌트가 변경되었다는 사실을 알 수가 없으므로
	해당 컴포넌트를 구독해놓고, 변경될 때마다 발행을 요청하는 모델
	(여러개의 컴포넌트들을 구독해놓고, 이벤트 발생할 때마다 바뀐 컴포넌트들을 반환)
*/
function createStore() {
	let state;
	let handlers = []; //구독함수들을 저장

	function send(action) { //3:상태를 원본 변화없이 전달만 하는 함수인 send 호출 
		state = worker(state, action); //4:sned를 통해 상태를 바꾸는 함수인 worker 호출
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
		send, //6:worker를 통해 바꾼 state를 store함수에 return
		getState,
		subscribe,
	};
}

function worker(state = { count:0 }, action) { //5:worker로 상태를 원본 변화없이 상태값만 바꿈
	//상태를 바꾸는 함수
	switch(action?.type){
		case 'increase':
			return { ...state, count:state.count+1 }
		default :
			return {...state}
	}
}

const store = createStore(worker); //2:상태정보를 담고있는 store 호출

store.send() //1:상태바꾸는 신호 주기

store.subscribe(function(){ //데이터가 바뀔 때마다 console에 getState가 찍힘
	console.log(store.getState())
})

store.send({ type:'increase' }); //action의 type을 명시하는 것이 Redux의 약속
store.send({ type:'increase' });
store.send({ type:'increase' });
store.send({ type:'increase' });
console.log('hello')