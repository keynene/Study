// import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function Header(props){
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
function Create(props){
  return <article>
    <h2>Create</h2>
    <form onSubmit={event=>{
      event.preventDefault();
      const title = event.target.title.value;
      const body = event.target.body.value;
      props.onCreate(title,body);
    }}>
      <p><input type="text" name="title" placeholder='title'/></p>
      <p><textarea name="body" placeholder='body'></textarea></p>
      <p><input type="submit" value="create"></input></p>
    </form>
  </article>
}
function Update(props){
  //props로 들어온 title값과 body값을 state로 환승
  //update시 값을 수정해야 하는데 props는 사용자 임의대로 값을 변경할 수 없기 때문에 state로 변경해줌
  const [title, setTitle] = useState(props.title); 
  const [body, setBody] = useState(props.body);
  return <article>
    <h2>Update</h2>
    <form onSubmit={event=>{
      event.preventDefault();
      const title = event.target.title.value;
      const body = event.target.body.value;
      props.onUpdate(title,body);
    }}>
      <p><input type="text" name="title" placeholder='title' value={title} onChange={event=>{
        setTitle(event.target.value); //props → state로 환승한 값을 임의의 title로 세팅 
      }}/></p>
      <p><textarea name="body" placeholder='body' value={body} onChange={event=>{
        setBody(event.target.value);
      }}></textarea></p>
      <p><input type="submit" value="update"></input></p>
    </form>
  </article>
}
function App(){
  const [mode, setMode] = useState('WELCOME'); //0번쨰 인자는 'WELCOME'저장, 1번쨰 인자는 함수로 사용
  const [id, setId] = useState(null);
  const [nextId, setnextId] = useState(4);
  const [topics,setTopics] = useState([
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'js', body:'javascript is ...'}
  ]);
  /* html, css, javascript 중에 어떤것을 선택했는지 확인하여 해당 값을 전달 */
  let content = null;
  let contextControl = null;
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
    contextControl = <li><a href={'/update/'+id} onClick={event=>{
      event.preventDefault();
      setMode('UPDATE');
    }}>Update</a></li>;
  } else if(mode === 'CREATE'){
    content = <Create onCreate={(_title,_body)=>{
      const newTopic = {id:nextId, title:_title, body:_body}
      const newTopics = [...topics] // topics 복제함
      newTopics.push(newTopic);
      setTopics(newTopics);
      setMode('READ');
      setId(nextId);
      setnextId(nextId+1);
    }}></Create>
  } else if(mode === 'UPDATE'){
    let title, body = null;
    for(let i=0; i<topics.length; i++){
      if(topics[i].id === id){ 
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Update title={title} body={body} onUpdate={(_title,_body)=>{
      const newTopics = [...topics]
      const updatedTopic = {id:id, title:_title, body:_body}
      for (let i=0; i<newTopics.length; i++){
        if(newTopics[i].id === id){
          newTopics[i] = updatedTopic;
          break;
        } 
      }
      setTopics(newTopics);
      setMode('READ');
    }}></Update>
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
      <ul>
        <li><a href="/create" onClick={event=>{
          event.preventDefault();
          setMode('CREATE');
        }}>Create</a></li>
        {contextControl}
      </ul>
    </div>
  );
}
 
export default App;