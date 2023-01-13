/* eslint-disable */ //warning 제거

import { useContext, useEffect, useState } from "react";
import { Nav } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { addCart } from "./../store.js";
import { useParams } from "react-router-dom";
import styled from 'styled-components';
import { Context1 } from '../App.js' //App.js에서 Detail.js로 공유받고싶은 state import
import store from "./../store.js";

let YellowBtn = styled.button`
  background : ${ props => props.bg };
  color : ${ props => props.bg == 'blue' ? 'white' : 'black' };
  padding : 10px;
  `
  // bg가 blue이면 color white, 아니면 color black

function Detail(props){
  // useParams() : 유저가 URL파라미터에 입력한 값 가져와줌 (파라미터 사용하기)
  let {id} = useParams();
  let product = props.shoes.find((x)=>{ return x.id == id });
  // let product = props.shoes.find( x => x.id == id)

  let [over, setOver] = useState(true); //2초이내 구매페이지 유무
  let [isdigit, setIsdigit] = useState(''); //숫자입력 인풋창 밸류값
  let [protab, setProtab] = useState(0); //탭변경
  let [fade, setFade] = useState('');

  //최근 본 상품 : localStorage에 저장
  useEffect(()=>{
    //localStorage는 수정이 안 되니까 저장된 정보를 꺼내서 업데이트하고 다시 넣어줘야 함
    let watchedData = localStorage.getItem('watched')
    watchedData = JSON.parse(watchedData)
    watchedData.push(product.id)
    //중복제거하기
    watchedData = new Set(watchedData) //집합으로 만들었다가
    watchedData = Array.from(watchedData) //배열로 바꾸기
    localStorage.setItem('watched', JSON.stringify(watchedData))
  },[])
      
  useEffect(()=>{
    // 페이지가 mount, update 마다 코드 실행
    let a = setTimeout(()=>{ setOver(false) }, 2000)
    setTimeout(()=>{ setFade('end') }, 10)

    if (isNaN(isdigit) == true){ alert('숫자만 입력해주세요') }
    return ()=>{ 
      clearTimeout(a)
      // setFade('')
     }

  }, [isdigit]); //isdigit 내용 바뀔 때마다 useEffect()실행

  return(
    <div className={`start ${fade}`}>
      <div className="container">
        {
          //useEffect()예제 : 2초이내 구매페이지 유무
          over == true 
          ?
            <div className="alert alert-warning">
              2초이내 구매시 할인
            </div>
          : null
        }


        {/*  sytled-components 예제
        <YellowBtn bg="blue">버튼</YellowBtn>
        <YellowBtn bg="orange">버튼</YellowBtn> 
        */}

        {/* 제품상세UI */}
        <div className="row">
          <div className="col-md-6">
            <img src={"https://codingapple1.github.io/shop/shoes"+(product.id+1)+".jpg"} width="100%" />
          </div>
          <div className="col-md-6">
            <h4 className="pt-5">{product.title}</h4>
            <p>{product.content}</p>
            <p>{product.price}원</p>
            <button className="btn btn-danger" onClick={()=>{
              //새로운 상품이 cart state에 추가되는 기능
              dispatch(addCart(product))
            }}>장바구니</button> 
          </div>
        </div>

        {/* 숫자입력 인풋창 */}
        <div className="input_num">
          <input onChange={(e)=>{ setIsdigit(e.target.value) }} placeholder="숫자만 입력해주세요" />
          {/* <input id="number" onChange={()=>{ setIsdigit(document.getElementById("number").value) }} /> */}
        </div>

        {/* Tabs */}
        <Nav variant="tabs" defaultActiveKey="link0">
          <Nav.Item>
            <Nav.Link eventKey="link0" onClick={()=>{ setProtab(0) }} >버튼0</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="link1" onClick={()=>{ setProtab(1) }} >버튼1</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="link2" onClick={()=>{ setProtab(2) }} >버튼2</Nav.Link>
          </Nav.Item>
        </Nav>

        {/* TabContent */}
        <TabsContent protab={protab} />

      </div>
    </div>
  )
}

function TabsContent({protab}) {

  let [fade, setFade] = useState('')
  useEffect(()=>{
    let a = setTimeout(()=>{ setFade('end') }, 10)
    //setFade('end')만 하면 중복코드라고 인식해서 setFade('')와 동시에 실행됨
    
    return ()=>{ 
      setFade('')
      clearTimeout(a)
     }
  },[protab])

  //opacity 주기위해 div로 감쌈
  return (
    <div className={`start ${fade}`} >
      {/* {"start "+fade} 랑 똑같음 */}
      { [<div>내용0</div>,<div>내용1</div>,<div>내용2</div>][protab] }
    </div>
  )
}



export default Detail;