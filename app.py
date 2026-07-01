import json


def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []



def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)



def list_youtube_video(videos):
    print("\n")
    print("*"*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*"*70)
      


def add_video(videos):
    name=input("Enter video name ")
    time=input("Enter video time ")
    videos.append({'name': name,'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_youtube_video(videos)
    index=int(input("Enter the index of the video : "))
    if 1<= index <= len(videos):
        name = input("Enter the name of the update video : ")
        time = input("Enter the time of the updated video : ")
        videos[index-1]={'name' : name, 'time' : time}
        save_data_helper(videos)
    else:
        print("Invalid index entered")




def delete_video(videos):
    list_youtube_video(videos)
    index=int(input("Enter the index of the video to be deleted : "))
    if 1<= index <= len(videos):
        try: 
            del videos[index-1]
            save_data_helper(videos)
            print("Video is deleted sucessfully")
        except :
            print("Exception occured")
    else:
        print("Invalid Index")




def main():
    videos=load_data()
    while True:
        print("\n")
        print("--"*70)
        print("Youtube Manger | Choose an option ")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a video")
        print("5. Exit the app")

        choice= input("Enter your choice : ")
        # print(videos)

        match choice:
            case "1":
                list_youtube_video(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()

