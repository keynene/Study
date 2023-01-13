import { memo, useMemo, useState } from "react"

function Memo(){
	//버튼 누를때마다 재렌더링 되게 만들려고 state 생성함
	let [count, setCount] = useState(0)

	//useEffect()처럼 useMemo()사용
	let result = useMemo(()=>{ return ChildUseMemo() }, [])// []안에 state 넣으면 됨

	return (
		<div>
			<div className="alert alert-warning" >
				<h4>memo, useMemo 연습하는 페이지</h4>
				<p>페이지 재렌더링 될 때마다(아래 버트 누를 때마다) console에 "재렌더링됨" 찍힐꺼임</p>
				<p>상위 컴포넌트 재렌더링 될 때마다 하위 컴포넌트까지 재렌더링 되는데? 🤷🏻‍♀️</p>
				<br/>
				<p>👉🏻memo 기능 사용!</p>
				<p>자식 컴포넌트를 메모에 넣어 사용 (자식컴포넌트의 props가 변할때만 자식컴포넌트 재렌더링함)</p>
			</div>
			<ChildMemo />
			<button onClick={()=>{ setCount(count+1) }}>memo🙆🏻‍♀️</button>
		</div>

	)
}

let ChildMemo = memo( function(){
	console.log('재렌더링됨')
	return <div className="alert alert-danger"><h4>자식컴포넌트임</h4></div>
} )

function ChildUseMemo(){
	let cnt = 0;
	let i;
	
	for(i=0; i<1e9; i++){ cnt++ } //컴포넌트 실행할때마다 오래걸림
}

export default Memo