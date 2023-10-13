import React, { useContext, useState } from "react";

import { Modal, Form, Button } from "react-bootstrap";
import { getUser } from "../../hooks/user.action";
import axiosService from "../../helpers/axios";
import { Context } from "../Layout";

const CreatePost = (props) => {
  const { setToaster } = useContext(Context);

  const { refresh } = props;
  const [show, setShow] = useState(false);
  const [form, setForm] = useState({});

  const [validated, setValidated] = useState(null);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const user = getUser();

  //
  const handleSubmit = (event) => {
    event.preventDefault();
    const createPostForm = event.currentTarget;

    if (createPostForm.checkValidity() === false) {
      event.stopPropagation();
    }

    setValidated(true);

    const data = {
      author: user.id,
      body: form.body,
    };

    axiosService
      .post("/post/", data)
      .then(() => {
        handleClose();
        setToaster({
          title: "Post",
          show: true,
          message: "Post created 🚀",
          type: "success",
        });
        setForm({});
        refresh();
      })
      .catch(() => {
        setToaster({
          title: "Post",
          show: true,
          message: "An error occurred. 🚀",
          type: "danger",
        });
      });
  };

  return (
    <>
      <Form.Group className="my-3 w-75">
        <Form.Control
          className="py-2 rounded-pill border-primary text-primary"
          type="text"
          placeholder="Write a post"
          onClick={handleShow}
        />
      </Form.Group>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton className="border-0">
          <Modal.Title>Create Post</Modal.Title>
        </Modal.Header>
        <Modal.Body className="border-0">
          <Form noValidate validated={validated} onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Control
                name="body"
                value={form.body}
                onChange={(e) => setForm({ ...form, body: e.target.value })}
                as="textarea"
                rows={3}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button
            variant="primary"
            onClick={handleSubmit}
            disabled={form.body === undefined}
          >
            Post
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default CreatePost;
