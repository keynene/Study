/* eslint-disable */ //warning 제거

import { useParams } from "react-router-dom";
import styled from 'styled-components';

let YellowBtn = styled.button`
  background : ${ props => props.bg };
  color : ${ props => props.bg == 'blue' ? 'white' : 'black' };
  padding : 10px;
  `
  // bg가 blue이면 color white, 아니면 color black

let NewBtn = styled.button(YellowBtn)`
  padding : 20px;
`
//기존 스타일 복사가능 물론 ``로 스타일 추가도 가능



function Detail(props){

    // useParams() : 유저가 URL파라미터에 입력한 값 가져와줌
    let {id} = useParams();
    let product = props.shoes.find((x)=>{
        return x.id == id
    })

    return(
        <div className="container">
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
        </div>
    )
}

export default Detail;