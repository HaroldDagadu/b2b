import React, { useEffect, useState } from 'react';
import { MDBContainer, MDBRow, MDBCol, MDBCard, MDBCardBody, MDBCardText, MDBBtn } from 'mdb-react-ui-kit';
import api from './api'; // Axios instance
import Navbar from './navbar'; // Custom Navbar
import PostCreationForm from './post'; // Import your existing PostCreationForm component

const Homepage = () => {
  const [posts, setPosts] = useState([]);
  const [showForm, setShowForm] = useState(false); // State to control visibility of the form

  useEffect(() => {
    fetchPosts();
  }, []);

  // Fetch posts from the API
  const fetchPosts = async () => {
    try {
      const response = await api.get('/api/b2bposts/'); // Correct endpoint for fetching posts
      setPosts(response.data);
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  };

  // Handle like or dislike actions
  const handleAction = async (postId, action) => {
    try {
      const response = await api.post(`/api/b2bposts/${postId}/${action}/`); // Correct endpoint for updating posts
      setPosts(posts.map(post => (post.id === postId ? response.data : post)));
    } catch (error) {
      console.error(`Error updating post ${action}:`, error);
    }
  };

  // Toggle the visibility of the post creation form
  const toggleForm = () => {
    setShowForm(!showForm);
  };

  return (
    <>
      <Navbar /> {/* Custom Navbar */}

      <MDBContainer>
        <div className="text-center my-4">
          <MDBBtn color="black" onClick={toggleForm}>
            {showForm ? "Hide Post Creation Form" : "Create New Post"}
          </MDBBtn>
        </div>

        {/* Conditionally render the PostCreationForm */}
        {showForm && (
          <MDBContainer fluid className="p-5 my-5 d-flex justify-content-center align-items-center h-custom">
            <MDBContainer className="shadow-lg rounded-5 login-form-container p-5 bg-white" lg='9'>
              <PostCreationForm fetchPosts={fetchPosts} /> {/* Pass fetchPosts to PostCreationForm to refetch posts after creation */}
            </MDBContainer>
          </MDBContainer>
        )}

        <div>
          <h1>Statements</h1>
        </div>
        <div>
          <h1>APP IS UNDER CONSTRUCTION, NOTHING WORKS 👷🏗️🚧</h1>
        </div>
        <MDBRow>
          {posts.map(post => (
            <MDBCol md="4" key={post.id} className="mb-4">
              <MDBCard className="h-100 shadow-sm">
                <MDBCardBody>
                  <MDBCardText>{post.content}</MDBCardText>
                  <div className="d-flex justify-content-between align-items-center">
                    <div>
                      {/* Like Button */}
                      <MDBBtn
                        color="success"
                        size="sm"
                        onClick={() => handleAction(post.id, 'fact')} // Action "fact" for likes
                      >
                        👍 Fact {post.facts}
                      </MDBBtn>
                      {/* Dislike Button */}
                      <MDBBtn
                        color="danger"
                        size="sm"
                        onClick={() => handleAction(post.id, 'nah_bro')} // Action "nah_bro" for dislikes
                        className="ms-2"
                      >
                        👎 Nah {post.nah_bro}
                      </MDBBtn>
                    </div>
                  </div>
                </MDBCardBody>
              </MDBCard>
            </MDBCol>
          ))}
        </MDBRow>
      </MDBContainer>
    </>
  );
};

export default Homepage;
