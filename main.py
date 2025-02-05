import flet as ft

width = 625
height = width

def main(page: ft.Page):

    def reset_game(grid, all_tiles, turn_text, page):
        for i in range(9):
            grid[i] = str(i + 1) #Reset grid
        
        for tile in all_tiles:
            tile.content.value = ""
            tile.bgcolor = ft.Colors.AMBER
            tile.on_click = lambda e, t=tile: player_turn(t, turn_text, all_tiles)
            tile.update()
        
        turn_text.value = "It is X's turn"
        turn_text.color = ft.Colors.RED
        turn_text.update()
        page.update()

    def check_win(grid, all_tiles, turn_text):
        win_condition = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        win = False

        for condition in win_condition:
            if grid[condition[0]] == grid[condition[1]] == grid[condition[2]] and grid[condition[0]] != "":
               turn_text.value = f'{grid[condition[0]]} has won.'
               turn_text.color = ft.Colors.AMBER_200
               win = True
               turn_text.update()
               for tile in all_tiles:
                   tile.on_click = None
                   tile.update()

        if not win and all(tile.content.value != "" for tile in all_tiles):
            turn_text.value = "It was a draw"
            turn_text.color = ft.Colors.AMBER_200
            turn_text.update()

    def player_turn(tile, turn_text, all_tiles):
        if tile.content.value == "":
            if 'O' in turn_text.value:
                turn_text.value = "It is X's turn"
                turn_text.color = ft.Colors.RED
                tile.bgcolor = ft.Colors.BLUE
                tile.content.value = 'O'
                grid[int(tile.data)] = tile.content.value

            else:
                turn_text.value = "It is O's turn"
                turn_text.color = ft.Colors.BLUE
                tile.bgcolor = ft.Colors.RED
                tile.content.value = 'X'
                grid[int(tile.data)] = tile.content.value
            
            tile.content.color = ft.Colors.BLACK
            tile.content.size = 25
            tile.on_click = None
            tile.update()
            turn_text.update()        
            
        check_win(grid, all_tiles, turn_text)
            
        return None

    global grid
    grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    page.title = 'TIC - TAC - TOE'
    page.window.width = width
    page.window.height = height

    turn_text = ft.Text(value = "It is X's turn", size = 20, color = ft.Colors.RED )

    title = ft.Text(value = 'TIC - TAC - TOE', color = ft.Colors.PINK_200, size = 34)
    
    divider = ft.Divider(thickness=5, color=ft.Colors.TRANSPARENT)

    def tiles(value):
        tile = ft.Container(
            content=ft.Text(""),
            data=f'{value}',
            margin=5,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.AMBER,
            width=width/(width/100),
            height=width/(width/100),
            border_radius=10,
            ink=True,
            on_click = lambda e: player_turn(tile, turn_text, all_tiles)
        )
        return tile
    
    tile_1 = tiles(0)
    tile_2 = tiles(1)
    tile_3 = tiles(2)
    tile_4 = tiles(3)
    tile_5 = tiles(4)
    tile_6 = tiles(5)
    tile_7 = tiles(6)
    tile_8 = tiles(7)
    tile_9 = tiles(8)

    all_tiles = [tile_1, tile_2, tile_3, tile_4, tile_5, tile_6, tile_7, tile_8, tile_9]

    row_0 = ft.Row([tile_1, tile_2, tile_3], alignment=ft.MainAxisAlignment.CENTER)
    row_1 = ft.Row([tile_4, tile_5, tile_6], alignment=ft.MainAxisAlignment.CENTER)
    row_2 = ft.Row([tile_7, tile_8, tile_9], alignment=ft.MainAxisAlignment.CENTER)

    reset = ft.ElevatedButton(text="Reset Game", on_click=lambda e: reset_game(grid, all_tiles, turn_text, page))

    app_page = ft.Container(
        content = ft.Column(
            controls = [
                ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
                divider,
                row_0,
                row_1,
                row_2,
                divider,
                ft.Row([turn_text], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([reset], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    )

    body = ft.Container(
        content = ft.Column(controls=[app_page]),
        width = width,
        height = height,
        alignment = ft.MainAxisAlignment.CENTER
    )

    page.add(body)

ft.app(main)
