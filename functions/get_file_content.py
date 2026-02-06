import os

def get_file_content(working_directory, file_path):
    try:
        p = os.path.abspath(working_directory)
        x = os.path.join(p, file_path)
        normalized_x = os.path.normpath(x)
        absolute_normal = os.path.abspath(normalized_x)
        if os.path.commonpath([p, normalized_x]) == p:
            if not os.path.isfile(absolute_normal):
                return f'Error: File not found or is not a regular file "{file_path}"'
            MAX_CHARS = 10000

            with open(absolute_normal, "r") as f:
                content = f.read(MAX_CHARS)
                if f.read(1) != "":
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
        else:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
    except Exception as e:
        return f"Error: {e}"
