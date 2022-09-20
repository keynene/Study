import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function Header(props){
  console.log('props', props.title);
  return <header>
    <h1><a href="/" onClick={(event)=>{
      event.preventDefault(); //a만의 기본속성 제거 (페이지 reload)
      props.onChangeMode(); //App() 의 함수를 호출
    }}>{props.title}</a></h1>
  </header>
}
function Nav(props){
  const lis=[];
  for(let i=0; i<props.topics.length; i++){
    let t = props.topics[i];
    lis.push(<li key={t.id}>
      <a id={t.id} href={'/read/'+t.id} onClick={(event)=>{
        event.preventDefault();
        props.onChangeMode(Number(event.target.id)); //event를 유발시킨 태그를 의미
      }}>{t.title}</a>
    </li>)
  }
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}
function Article(props){
  return <article>
    <h2>{props.title}</h2>
    {props.body}
  </article>
}
function App(){
  const [mode, setMode] = useState('WELCOME'); //0번쨰 인자는 'WELCOME'저장, 1번쨰 인자는 함수로 사용
  const [id, setId] = useState(null);
  const topics = [
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'js', body:'javascript is ...'}
  ];
  /* html, css, javascript 중에 어떤것을 선택했는지 확인하여 해당 값을 전달 */
  let content = null;
  if(mode === 'WELCOME'){
    content = <Article title="Welcome" body="Hello, WEB"></Article>;
  } else if(mode === 'READ'){
    let title, body = null;
    for(let i=0; i<topics.length; i++){
      if(topics[i].id === id){ 
        //topics의 id에 저장된 값과 nav에서 클릭하여 setId를 통해 변경된 상태의 (_id)값을 비교하여 동일한 값 찾아 
        //topics에 저장된 topics[i].title과 topics[i].body값을 각 변수(title, body)에 저장
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body={body}></Article>;
  }
  return (
    <div>
      <Header title="WEB" onChangeMode={()=>{
        setMode('WELCOME'); //setMode를 통해 상태값이 'WELCOME'으로 바뀜
      }}></Header>
      <Nav topics={topics} onChangeMode={(_id)=>{
        setMode('READ'); //setMode를 통해 상태값이 'READ'로 바뀜
        setId(_id);
      }}></Nav>
      {content}
      {/* <Article title="Welcome" body="Hello, WEB"></Article> */}
    </div>
  );
}
 
export default App;