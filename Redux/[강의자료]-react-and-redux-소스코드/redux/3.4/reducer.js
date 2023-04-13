export function reducer(state = { count: 0 }, action) {
  // do something
  switch(action.type) {
    case 'increase':
      return { ...state, count: state.count + 1 };
    default: 
      return { ...state };
  }
}