def main():
    st.set_page_config(layout="wide")
    st.title("🚀 Fast RAG-based QA with DeepSeek R1")
    
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        
        if uploaded_file:
            try:
                image_path = get_pdf_first_page_image(uploaded_file)
                st.image(image_path, caption="First Page Preview", use_column_width=True)
            except Exception as e:
                st.error("Failed to load preview: " + str(e))
    
    if uploaded_file:
        with st.spinner("🔄 Processing PDF..."):
            retriever = process_pdf(uploaded_file)
        
        llm = get_llm()
        qa_chain = build_qa_chain(retriever, llm)
        
        user_input = st.text_input("Enter your question:")
        
        if user_input:
            with st.spinner("🤖 Generating response..."):
                #response = qa_chain.invoke({"query": user_input})["result"]
                st.write("### 📜 Answer:")
                st.write(response)
    else:
        st.info("📥 Please upload a PDF file to proceed.")
