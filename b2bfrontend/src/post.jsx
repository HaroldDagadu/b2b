import React, { useState } from 'react';
import {
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardHeader,
  MDBCardFooter,
  MDBIcon,
  MDBTextArea
} from 'mdb-react-ui-kit';
import api from './api'; // Assuming 'api.js' sets up axios with credentials

const PostCreationForm = () => {
  const [content, setContent] = useState('');
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Reset error state
    setIsSubmitting(true); // Set submitting state to true

    try {
      const response = await api.post('/api/b2bposts/', {
        content, // Post content from the form
      });

      if (response.status === 201) {
        // Successfully created post
        setContent(''); // Clear content after successful creation
        alert('Post created successfully!');
      } else {
        throw new Error('Failed to create post');
      }
    } catch (err) {
      // Handle error and update the state
      setError('Failed to create post. Please try again.');
    } finally {
      setIsSubmitting(false); // Reset submitting state
    }
  };

  return (
    <MDBCard>
      <MDBCardHeader>
        <h4>Create a New Post</h4>
      </MDBCardHeader>
      <form onSubmit={handleSubmit}>
        <MDBCardBody>
          {/* Error Alert */}
          {error && (
            <div className="alert alert-danger d-flex align-items-center" role="alert">
              <MDBIcon fas icon="exclamation-triangle" className="me-2" />
              {error}
            </div>
          )}

          {/* Post Content Textarea */}
          <MDBTextArea
            label="What's on your mind?"
            placeholder="Share your thoughts here (Max 200 characters)"
            rows={4}
            maxLength={200}
            value={content}
            onChange={(e) => setContent(e.target.value)}
            disabled={isSubmitting}
            required
          />

          {/* Character Count */}
          <div className="text-end text-muted mt-2">
            {content.length}/200
          </div>
        </MDBCardBody>

        <MDBCardFooter className="d-flex justify-content-end">
          {/* Cancel Button */}
          <MDBBtn
            color="light"
            type="button"
            onClick={() => setContent('')} // Clear content on cancel
            disabled={isSubmitting}
            className="me-2"
          >
            Cancel
          </MDBBtn>

          {/* Submit Button */}
          <MDBBtn
            color="primary"
            type="submit"
            disabled={!content.trim() || isSubmitting} // Disable button if no content or submitting
          >
            {isSubmitting ? 'Posting...' : 'Post'}
          </MDBBtn>
        </MDBCardFooter>
      </form>
    </MDBCard>
  );
};

export default PostCreationForm;
