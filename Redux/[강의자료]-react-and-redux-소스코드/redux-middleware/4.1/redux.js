export const actionCreator = type => payload => ({
  type,
  payload,
});

export function createStore(reducer, middlewares = []) {
  let state;
  const handlers = [];

  //1. action을 실행시켜주는 dispatch 동작은 createStore를 통해 state를 만들어놓고,
  //추후에 dispatch를 통해 필요할 때 실햄됨
  function dispatch(action) {
    state = reducer(state, action);
    handlers.forEach(handler => handler());
  }

  function getState() {
    return state;
  }

  function subscribe(handler) {
    handlers.push(handler);
  }
  
  const store = {
    getState,
    subscribe,
    dispatch,
  };

  //6. 실행해보면 middleware가 역순으로 실행되는데 이걸 막기 위해 처음부터 역순으로 저장해서 넣어주기
  middlewares = Array.from(middlewares).reverse() //원본 훼손하지 않기 위해 Array.from으로 [...]효과주기
  
  //3. middleware를 비동기적으로 만들기 위한, dispatch호출을 필요할 때 사용 및 실행되도록 하기위한 함수
  let lastDispatch = dispatch;
  


  //2. 반면에 middleware는 createStore를 통해 state가 만들어짐과 동시에 forEach문을 통해
  //바로 실행되어버림
  //이를 비동기적으로 필요할 때마다 실행되게 하기위해 "Currying"문법이 필요함!
  //Currying은 함수를 매개변수로 전달해, 표현에 풍부함이 있음과 동시에
  //기본적으로 "호출을 지연"시킨다는 장점이 있음!
  middlewares.forEach(middleware => {
    //4. action까지 주면 바로 실행되어 버리니까 action은 필요 시에만 전달하도록 코딩할꺼임
    lastDispatch = middleware(store)(lastDispatch); 
  })

  //5. lastDispatch에 들어간 마지막 dispatch 값이 dispatch에 저장됨
  store.dispatch = lastDispatch;


  return store;
}
