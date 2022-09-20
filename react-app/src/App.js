import logo from './logo.svg';
import './App.css';
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
        props.onChangeMode(event.target.id); //event를 유발시킨 태그를 의미
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
  const topics = [
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'js', body:'javascript is ...'}
  ];
  return (
    <div>
      <Header title="WEB" onChangeMode={()=>{
        alert('Header');
      }}></Header>
      <Nav topics={topics} onChangeMode={(id)=>{
        alert(id);
      }}></Nav>
      <Article title="Welcome" body="Hello, WEB"></Article>
    </div>
  );
}
 
export default App;