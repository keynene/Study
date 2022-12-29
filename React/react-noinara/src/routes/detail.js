/* eslint-disable */ //warning 제거

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import styled from 'styled-components';

let YellowBtn = styled.button`
  background : ${ props => props.bg };
  color : ${ props => props.bg == 'blue' ? 'white' : 'black' };
  padding : 10px;
  `
  // bg가 blue이면 color white, 아니면 color black

function Detail(props){
    
  // useParams() : 유저가 URL파라미터에 입력한 값 가져와줌 (파라미터 사용하기)
  let {id} = useParams();
  let product = props.shoes.find((x)=>{
    return x.id == id
  })
  // let product = props.shoes.find( x => x.id == id)

  let [over, setOver] = useState(true)

  let [isdigit, setIsdigit] = useState('');
      
  useEffect(()=>{
    // 페이지가 mount, update 마다 코드 실행
    let a = setTimeout(()=>{ setOver(false) }, 2000)

    if (isNaN(isdigit) == true){
        alert('숫자만 입력해주세요')
    }
    
    return ()=>{
        clearTimeout(a)
    }
  }, [isdigit]);

  return(
    <div className="container">
      {
        //useEffect()예제
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

      <div className="row">
        <div className="col-md-6">
          <img src={"https://codingapple1.github.io/shop/shoes1.jpg"} width="100%" />
        </div>
        <div className="col-md-6">
          <h4 className="pt-5">{product.title}</h4>
          <p>{product.content}</p>
          <p>{product.price}원</p>
          <button className="btn btn-danger">주문하기</button> 
        </div>
      </div>

      <input onChange={(e)=>{ setIsdigit(e.target.value) }} />
      {/* <input id="number" onChange={()=>{ setIsdigit(document.getElementById("number").value) }} /> */}

    </div>
  )
}

export default Detail;