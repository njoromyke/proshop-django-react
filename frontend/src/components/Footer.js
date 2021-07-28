import React from 'react'
import { Container,Row,Col } from 'react-bootstrap'
const Footer = () => {
    return (
        <footer>
            <Container>
                <Row>
                    <Col md={12 } className="text-center py-3">
                        Copy &copy; mykesoftware
                    </Col>
                </Row>
            </Container>

           
        </footer>
    )
}

export default Footer
